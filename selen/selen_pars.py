# -*- coding: utf8 -*

from re import search, split

from selen_logging import log_save
from selen_selenium import click, input_keys
from selen_assert import assert_url, assert_field
from SelenStep import SelenStep


def open_file_r(filename:str, enc="utf8") -> list:
    
    file_list = []
    file_list_append = file_list.append

    with open(filename, "r", encoding=enc) as my_file:
        for line in my_file:
            file_list_append(line)
    my_file.close()

    return file_list


def add_data(step:object, data:list) -> object:

    func_name = step.action

    if (search(r"^click", func_name)):
        step.action = "click"
        step.xpath = data[2].strip()
        step.func = click       
        
    elif (search(r"^input", func_name)):
        step.action = "input"
        step.xpath = data[2].strip()
        step.data = data[3].strip()
        step.func = input_keys

    elif (search(r"^url", func_name)):
        step.action = "url"
        step.data = data[2].strip()
        step.func = assert_url

    elif (search(r"^return", func_name)):
        step.action = "return"

    elif (search(r"^expect", func_name)):
        step.action = "expect"
        step.xpath = data[2].strip()
        step.data = data[3].strip()
        step.func = assert_field
        
    return step


def test_parsing(testpath:str) -> list:

    tests_data = open_file_r(testpath)
    final_data = []
    step = None

    final_data_append = final_data.append
    
    for string in tests_data:
        serch_res = search(r"^;.*;.*;.*;", string)
        if serch_res:
            lst = string.split(";")
            step = SelenStep(lst[1])
            final_data_append(add_data(step, lst))

    return final_data
