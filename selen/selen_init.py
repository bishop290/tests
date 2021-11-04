# -*- coding: utf8 -*

from multiprocessing import Process
#import functools

from selen_pars import test_parsing
from selen_selenium import get_new_test, start_browser, open_url


def start(test_info:object):

    test_obj = get_new_test(test_info.name)
    start_browser(test_obj, test_info.browser)
    open_url(test_obj, test_info.url)

    for step in test_info.tests:
        func = step.func
        if (step.action == "input"):
            func(test_obj, step.xpath, step.input_data)
        else:
            func(test_obj, step.xpath)

    test_obj.browser.quit()
    

def init(tests:tuple):

    procs = []
    for test_info in tests:
        test_info.tests = test_parsing(test_info.path)
        proc = Process(target=start, args=(test_info,))
        procs.append(proc)

    for proc in procs:
        proc.start()
        proc.join()
        
        

    
    
