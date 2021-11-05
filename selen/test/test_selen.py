# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, '..') # подключение каталога на уровень выше


from SelenOpt import SelenOpt
from selen_init import init 


def main():

    

    first_url = "https://www.selenium.dev/selenium/docs/api/py/api.html"
    first_path = "C:\\test\\test-data"
    first = SelenOpt("First", first_url, first_path, "chrome")
    second = SelenOpt("Second", first_url, first_path, "firefox")
    
    tests = ( 
        first, #second,
    )
    
    init(tests)    
        
if __name__ == '__main__':
    sys.exit(main()) 


