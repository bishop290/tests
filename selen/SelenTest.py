# -*- coding: utf8 -*

from os import path, sep
from re import sub
from datetime import datetime


class SelenTest:
    
    def __init__(self, test_name:str, driver:object):
        self.name = test_name
        self.webdriver = driver
        self.browser = None
        self.logpath = self._get_default_logpath()
        self.logfile_name = self._get_logfile_name()
        self.logfile_fullpath = self._get_logfile_fullpath()

    def _get_default_logpath(self) -> str:
        return path.split(path.abspath(__file__))[0]

    def _get_logfile_name(self) -> str:
        dt = str(datetime.now())

        def rep(x:object) -> str:
            ch = x.group(0)
            if ch == "-" or ch == ":" or ch == ".":
                return "-"
            elif ch == " ":
                return "_"

        dt = sub(r"[-:. ]", rep, dt)
        name = sub(r"[ /\\:*?\"><+|.%@!]", r"", self.name)

        return 'log_{0}_{1}.txt'.format(name, dt)

    def _get_logfile_fullpath(self) -> str:
        return '{0}{1}{2}'.format(self.logpath, sep, self.logfile_name)
        
    def put_logpath(self, logpath:str):
        self.logpath = logpath
        self.logfile_fullpath = self._get_logfile_fullpath()

    def print_info(self) -> str:
        info = """
        Name         : {0}
        Driver       : {1}
        Logfile path : {2}"""
        return info.format(
            self.name,
            str(self.webdriver),
            self.logfile_fullpath)
