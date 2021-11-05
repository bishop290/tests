# -*- coding: utf-8 -*-

import sys

from selenium import webdriver

sys.path.insert(1, '..')
from selen_selenium import get_attributes
from SelenTest import SelenTest


def main(params:list):

     if (len(params) != 3):
          print("Не верное количество параметров")
          return

     url = params[1].strip()
     xpath = params[2].strip()
     
     test = SelenTest("Test", webdriver)
     test.logfile_fullpath = ""
     test.browser = test.webdriver.Chrome()
     test.browser.get(url)

     txt = """\n
    URL        : {0}
    INPUT      : {1}
    ATTRIBUTES : {2}
     """

     attr = get_attributes(test, xpath)
     print(txt.format(url, xpath, str(attr)))
     return
     

if __name__ == '__main__':
    sys.exit(main(sys.argv))
