#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

usage() {
  cat <<EOF
Usage: $(basename "${BASH_SOURCE[0]}") [-h] -p param_value arg1 [arg2...]

param_value - путь файла для записи настроенной таблици.

Применяет правила к iptables, записывает результат в указанный файл.

Available options:

-h, --help      Print this help and exit
-p, --param     Some param description
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # удалить все временные файлы создынные скриптом во время работы
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

# Пример:
# msg "This is a ${RED}very important${NOFORMAT} message, but not a script output value!"
msg() {
  echo >&2 -e "${1-}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -f | --flag) flag=1 ;; # example flag
    -p | --param) # example named parameter
      param="${2-}"
      shift
      ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
  [[ -z "${param-}" ]] && die "Missing required parameter: param"
  #[[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}

function check_binary() {
    if [[ $# -lt 1 ]]; then
        die 'Missing required argument to check_binary()!' 2
    fi

    if ! command -v "$1" > /dev/null 2>&1; then
        if [[ -n ${2-} ]]; then
            die "Missing dependency: Couldn't locate $1." 1
        else
            msg "Missing dependency: $1" "${RED}"
            return 1
        fi
    fi

    msg "Found dependency: $1"
    return 0
}

function run_as_root() {
    if [[ $# -eq 0 ]]; then
        die 'Missing required argument to run_as_root()!' 2
    fi

    if [[ ${1-} =~ ^0$ ]]; then
        local skip_sudo=true
        shift
    fi

    if [[ $EUID -eq 0 ]]; then
        "$@"
    elif [[ -z ${skip_sudo-} ]]; then
        sudo -H -- "$@"
    else
        die "Unable to run requested command as root: $*" 1
    fi
}

parse_params "$@"
setup_colors

msg "${RED}Read parameters:${NOFORMAT}"
msg "- flag: ${flag}"
msg "- param: ${param}"
msg "- arguments: ${args[*]-}"

check=1
check=$(check_binary iptables)
if [[ $check -eq  1 ]]; then
    die ""
fi

# очистить
run_as_root iptables --flush
run_as_root iptables --delete-chain

# политика по умолчанию:
run_as_root iptables --policy INPUT DROP
run_as_root iptables --policy OUTPUT DROP
run_as_root iptables --policy FORWARD DROP

# loopback
run_as_root iptables -A INPUT -i lo -j ACCEPT
run_as_root iptables -A OUTPUT -o lo -j ACCEPT

# ICMP (ping, tracerout)
run_as_root iptables -A INPUT -p icmp -j ACCEPT
run_as_root iptables -A OUTPUT -p icmp -j ACCEPT

# DNS
run_as_root iptables -A INPUT -p udp --sport 53 -m state --state ESTABLISHED -j ACCEPT
run_as_root iptables -A INPUT -p tcp --sport 53 -m state --state ESTABLISHED -j ACCEPT
run_as_root iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
run_as_root iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT

# Http, https, ssh
#run_as_root iptables -A INPUT -p tcp --dport 80 -j ACCEPT
#run_as_root iptables -A INPUT -p tcp --dport 443 -j ACCEPT
# run_as_root iptables -A INPUT -p tcp --dport 22 -j ACCEPT
#run_as_root iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT
#run_as_root iptables -A OUTPUT -p tcp --sport 443 -j ACCEPT
# run_as_root iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

# Statefull packet inspection (SPI)
run_as_root iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
run_as_root iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# apt
#run_as_root iptables -A INPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
#run_as_root iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT # такое правило уже было, так что это лишнее

# games
run_as_root iptables -A OUTPUT -m owner --gid-owner noinet -j LOG --log-prefix 'Group noinet: '
run_as_root iptables -A OUTPUT -m owner --gid-owner noinet -j DROP

# проверить добавление правил
run_as_root iptables -L -v --line-numbers

run_as_root /sbin/iptables-save > ${param}
