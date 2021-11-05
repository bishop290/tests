# -*- coding: utf8 -*

class SelenOpt:

    def __init__(self, name:str, url:str, path:str, browser:str):
        self.name = name.strip()
        self.url = url.strip()
        self.path = path.strip()
        self.browser = browser.strip()
        self.tests = None

    def print_info(self) -> str:
        info = """
        Name   : {0}
        Url    : {1}
        Path   : {2}
        Browser: {3}
        Tests  : {4}"""

        return info.format(
            self.name,
            self.url,
            self.path,
            str(self.browser),
            str(self.tests))
