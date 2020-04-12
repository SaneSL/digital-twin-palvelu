# Example module 2. Does division
from modules.module_abc import BaseModule


class Division(BaseModule):
    """DOCS 2"""
    module_id = 2
    def __init__(self, data_dict):
        self.upper = data_dict.get('upper')
        self.lower = data_dict.get('lower')

    # Make moduleArgException?
    def check_divider(self):
        if self.lower == 0:
            raise Exception    
    
    def divide(self):
        self.check_divider()
        results = sum(self.data)
        return {"data": results}

    def run(self):
        return self.divide()
