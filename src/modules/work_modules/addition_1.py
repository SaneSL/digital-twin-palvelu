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
    Raises
    ------
    ModuleArgError
        Raised if invalid arguments were given
    """
    module_id = 1
    def __init__(self, values):
        self._data = values # List

    def _add(self):
        try:
            results = sum(self._data)
            return {'data': results}
        except:
            raise ModuleArgError

    def _run(self):
        return self._add()


    