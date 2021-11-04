# -*- coding: utf8 -*

class SelenStep:
    
    def __init__(self, action:str, xpath:str, expect:str):
        self.action = action.strip()
        self.xpath = xpath.strip()
        self.expect = expect.strip()
        self.func = None
        self.input_data = None

    def print_info(self) -> str:

        info = """
Action  : {0}
Xpath   : {1}
Expect  : {2}
Function: {3}
Input   : {4}"""

        return info.format(
            self.action,
            self.xpath,
            self.expect,
            str(self.func),
            self.input_data
        )
    
