from modules.work_modules.addition_1 import Addition
from modules.work_modules.division_2 import Division
from utils.exceptions import ModuleNotFound, ModuleArgError

# pdoc --html --config show_source_code=False --output-dir static ./modules/work_modules --force

class ModuleFactory:
    modules = {1: Addition, 2: Division}

    @classmethod
    def get_module(cls, id, **kwargs):
        module = cls.modules.get(id, None)

        if module is None:
            raise ModuleNotFound
        else:
            try:
                return module(**kwargs)
            except:
                raise ModuleArgError