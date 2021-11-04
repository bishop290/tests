# -*- coding: utf8 -*

from re import search

from selen_logging import log_save
from selen_selenium import click, input_keys, click_with_return
from SelenStep import SelenStep


def open_file_r(filename:str, enc="utf8") -> list:
    
    file_list = []
    file_list_append = file_list.append

    with open(filename, "r", encoding=enc) as my_file:
        for line in my_file:
            file_list_append(line)
    my_file.close()

    return file_list


def add_func(step:object) -> object:

    func_name = step.action
    if (search(r"^click", func_name)):
        step.action = "click"
        step.func = click
        
    elif (search(r"^ret_", func_name)):
        step.action = "ret_click"
        step.func = click_with_return
        
    elif (search(r"^input", func_name)):
        step.func = input_keys
        step.input_data = func_name.split(":")[1].strip()
        step.action = "input"

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
            step = SelenStep(lst[1], lst[2], lst[3])
            final_data_append(add_func(step))

    return final_data
