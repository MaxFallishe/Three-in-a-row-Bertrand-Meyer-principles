from abc import ABC, abstractmethod


class AbstractGameEffect(ABC):
    @abstractmethod
    def apply(self):
        ...


class ShardVanishingEffect(AbstractGameEffect):
    def apply(self):
        ...
