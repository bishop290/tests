# -*- coding: utf8 -*

class SelenOpt:

    def __init__(self, name:str, url:str, path:str, browser:str):
        self.name = name.strip()
        self.url = url.strip()
        self.path = path.strip()
        self.browser = browser.strip()
        self.tests = None
