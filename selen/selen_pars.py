# -*- coding: utf8 -*

import re

from selen_logging import log_save
from selen_selenium import click, input_keys, click_with_return


def open_file_r(filename:str, enc="utf8") -> list:
    
    file_list = []
    file_list_append = file_list.append

    with open(filename, "r", encoding=enc) as my_file:
        for line in my_file:
            file_list_append(line)
    my_file.close()

    return file_list


def test_parsing(testpath:str) -> list:
    tests_data = open_file_r(testpath)
    final_data = []

    for string in tests_data:
        serch_res = re.search(r"^;.*;.*;.*;", string)
        if serch_res:
            print(string)
