# Example module 2. Does division
from modules.module_abc import BaseModule


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
    Exception
        [description]
    """
    module_id = 2
    def __init__(self, upper=None, lower=None):
        self._upper = upper
        self._lower = lower

    # Make moduleArgException?
    def _check_divider(self):
        if self._lower == 0:
            raise Exception    
    
    def _divide(self):
        self._check_divider()
        results = sum(self._data)
        return {"data": results}

    def _run(self):
        return self._divide()
