from abc import ABCMeta, abstractmethod

class BaseModule(metaclass=ABCMeta):
    @abstractmethod
    def _run(self):
        pass