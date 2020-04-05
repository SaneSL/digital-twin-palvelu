from modules.exmodule_1 import Addition
from modules.exmodule_2 import Division

class ModuleFactory:
    creators = {1: Addition, 2: Division}

    @classmethod
    def get_module(cls, id, data_dict):
        module = cls.creators.get(id)

        if module is None:
            raise ValueError
        else:
            return module(data_dict)