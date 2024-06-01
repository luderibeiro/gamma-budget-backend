from abc import ABCMeta, abstractmethod


class AbstractBaseOutput(metaclass=ABCMeta):
    """Base class for use cases output."""

    @property
    @abstractmethod
    def data(self) -> dict:
        pass

    @data.setter
    @abstractmethod
    def data(self, value: dict):
        pass
