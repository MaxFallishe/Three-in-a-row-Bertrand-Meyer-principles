from abc import ABC, abstractmethod


class AbstractGameEngine(ABC):
    @abstractmethod
    def ff(self):
        ...


class GameEngine(AbstractGameEngine):
    def ff(self):
        ...
