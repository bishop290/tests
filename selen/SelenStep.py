# -*- coding: utf8 -*

class SelenStep:
    
    def __init__(self, action:str):
        self.action = action.strip()
        self.xpath = None
        self.data = None
        self.func = None

    def print_info(self) -> str:

        info = """
        Action  : {0}
        Xpath   : {1}
        Data    : {2}        
        Function: {3}"""

        return info.format(
            self.action,
            self.xpath,
            self.data,
            str(self.func)
        )
    
