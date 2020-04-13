# Example module 1. Does addition
from modules.module_abc import BaseModule
from utils.exceptions import ModuleArgError, ModuleError

class Addition(BaseModule):
    """Calculates addition of given values
    
    Parameters
    ----------
    values : list
        List of values
    
    Returns
    -------
    int
        Result of addition
    """
    module_id = 1
    def __init__(self, values):
        self._data = values # List

    def _add(self):
        results = sum(self._data)
        return {'data': results}

    def _run(self):
        return self._add()


    