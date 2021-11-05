# -*- coding: utf8 -*

from selen_logging import log_save
from selen_selenium import get_text_in_field


def assert_url(test:object, url:str):
    current_url = test.browser.current_url

    if (current_url == url):
        log_save(test, "URL valid \n    ({0})".format(url), "info")
    else:
        txt = "URL invalid \n    (expect: {0}\n    real: {1})"
        log_save(test, txt.format(url, current_url), "error")
    

def assert_field(test:object, xpath:str, expect_text:str):
    actual_text = get_text_in_field(test, xpath)

    if (actual_text == expect_text):
        log_save(test, "Field text valid \n    ({0})".format(actual_text), "info")
    else:
        txt = "Field text invalid \n    (expect: {0}\n    real: {1})"
        log_save(test, txt.format(expect_text, actual_text), "error")
    
    
