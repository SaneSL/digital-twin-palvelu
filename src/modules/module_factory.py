from modules.work_modules.exmodule_1 import Addition
from modules.work_modules.exmodule_2 import Division

# pdoc --html --config show_source_code=False --output-dir docs . --force

class ModuleFactory:
    creators = {1: Addition, 2: Division}

    @classmethod
    def get_module(cls, id, data_dict):
        module = cls.creators.get(id)

        if module is None:
            raise ValueError
        else:
            return module(data_dict)