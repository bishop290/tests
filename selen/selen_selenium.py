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
    elif (browser == "firefox"):
        test.browser = test.webdriver.Firefox()
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


def get_attributes(test:object, pattern:str) -> dict:
    attr = {}

    element = find_element_xpath(test, pattern)
    if (element != None):
        js_code = """
        let attr = arguments[0].attributes;
        let items = {}; 
        for (let i = 0; i < attr.length; i++) {
            items[attr[i].name] = attr[i].value;
        }
        return items;
        """
    
        attr = test.browser.execute_script(js_code, element)

    return attr


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


def get_text_in_field(test:object, pattern:str) -> str:
    text = ""
    element = find_element_xpath(test, pattern)

    if (element != None):
       text = element.get_attribute('value')
        
    return text
