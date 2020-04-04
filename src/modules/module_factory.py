from modules.exmodule_1 import Addition
from modules.exmodule_2 import Division

class ModuleFactory:
    creators = {1: Addition, 2: Division}

    @classmethod
    def getModule(cls, id, **kwargs):
        Module = creators.get(id)

        if Module is None:
            raise ValueError
        else:
            return Module(**kwargs)