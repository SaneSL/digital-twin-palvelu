# Example module 2. Does division
from modules.module_abc import BaseModule


class Division(BaseModule):
    module_id = 2
    def __init__(self, **kwargs):
        self.upper = kwargs.get('upper')
        self.lower = kwargs.get('lower')

    # Make moduleArgException?
    def check_divider(self):
        if self.lower == 0:
            raise Exception    
    
    def divide(self):
        self.check_divider()
        results = sum(self.data)
        return results

    def run(self):
        return self.divide()
