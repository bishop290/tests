# -*- coding: utf8 -*

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException

from SelenTest import SelenTest
from selen_logging import log_save


def get_new_test(name:str) -> object:
    test = SelenTest(name, webdriver)
    log_save(test, test.print_info(), "info")
    return test


def start_browser(test:object, browser:str):
    if (browser == "chrome"):
        test.browser = test.webdriver.Chrome()
    test.browser.set_page_load_timeout(30)
    log_save(test, "Start " + browser, "info")

    
def open_url(test:object, url:str):
    test.browser.get(url)
    log_save(test, "Open " + url, "Info")


def find_element_xpath(test:object, pattern:str) -> object:
    element = None
    try:
        element = WebDriverWait(test.browser, 10).until(
            lambda x: x.find_element(By.XPATH, pattern)
        )
        log_save(test, 'Find element, pattern: {0}'.format(pattern), "info")
    except TimeoutException as ex:
        log_save(test, 'Not find element, pattern: {0}'.format(pattern), "error")
    except InvalidSelectorException as ex:
        log_save(test, 'Invalid pattern: {0}'.format(pattern), "error")

    return element


def click(test:object, pattern:str):
    element = find_element_xpath(test, pattern)
    if (element != None):
        element.click()
        log_save(test, "Element click, (pattern: {0})".format(pattern), "info")
        

def input_keys(test:object, pattern:str, keys:str):
    element = find_element_xpath(test, pattern)
    if (element != None):
        element.send_keys(keys)
        log_save(test, "Send keys, (pattern: {0}, keys: {1})".format(pattern, keys), "info")


def click_with_return(test:object, pattern:str):
    click(test, pattern)
    test.browser.back()

