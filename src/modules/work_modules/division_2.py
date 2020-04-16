# Example module 2. Does division
from modules.module_abc import BaseModule
from utils.exceptions import ModuleArgError, ModuleError

class Division(BaseModule):
    """Calculates division of two values
    
    Parameters
    ----------
    upper : int
        Divident
    lower : int
        Divisor
    
    Returns
    -------
    int
        Result of division
    
    Raises
    ------
    ModuleArgError
        Raised if invalid arguments were given
    """
    module_id = 2
    def __init__(self, upper=None, lower=None):
        self._upper = upper
        self._lower = lower

    def _check_divider(self):
        if self._lower == 0:
            raise ModuleArgError
    
    def _divide(self):
        self._check_divider()
        results = self._upper / self._lower
        return {"data": results}

    def _run(self):
        return self._divide()
