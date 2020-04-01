# Example module 1. Does addition
from modules.module_abc import BaseModule

class Addition(BaseModule):
    module_id = 1
    def __init__(self, data):
        self.data = data

    def add(self):
        results = sum(self.data)
        return results

    def run(self):
        return self.add()


    