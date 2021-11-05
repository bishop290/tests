# -*- coding: utf8 -*

from multiprocessing import Process

from selen_pars import test_parsing
from selen_selenium import get_new_test, start_browser, open_url
from selen_logging import log_save


def start(test_info:object):

    test_obj = get_new_test(test_info.name)

    log_save(test_obj, test_info.print_info(), "debug")
    
    start_browser(test_obj, test_info.browser)
    open_url(test_obj, test_info.url)

    log_save(test_obj, test_obj.print_info(), "debug")

    for step in test_info.tests:
        func = step.func

        log_save(test_obj, step.print_info(), "debug")

        if (step.action == "url"):
            func(test_obj, step.data)
        elif (step.action == "input" or step.action == "expect"):
            func(test_obj, step.xpath, step.data)
        elif (step.action == "click"):
            func(test_obj, step.xpath)
        elif (step.action == "return"):
            test_obj.browser.back()

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
