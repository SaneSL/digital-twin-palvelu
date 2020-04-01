from abc import ABCMeta, abstractmethod

class BaseModule(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass