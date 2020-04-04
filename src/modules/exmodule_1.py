# Example module 1. Does addition
from modules.module_abc import BaseModule

class Addition(BaseModule):
    module_id = 1
    def __init__(self, **kwargs):
        self.data = kwargs.get('data')

    def add(self):
        results = sum(self.data)
        return {'data': results}

    def run(self):
        return self.add()


    