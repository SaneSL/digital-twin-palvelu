# Main module which calls the other modules
# This makes the docstring easier

# Maybe make module parent that all modules subclass. This parent has get method to get the results so every child has it too. Maybe easier implementation?
# Use composition ig... or every method creates new instance of sub module? Factory thing?

from modules.module_factory import ModuleFactory


class ModuleAPI():
    def __init__(self):
        self.factory = ModuleFactory()