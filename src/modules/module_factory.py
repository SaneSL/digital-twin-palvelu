from modules.exmodule_1 import Addition
from modules.exmodule_2 import Division

class ModuleFactory:
    creators = {1: Addition, 2: Division}

    @classmethod
    def get_module(cls, id, **kwargs):
        module = cls.creators.get(id)

        if module is None:
            raise ValueError
        else:
            return module(**kwargs)