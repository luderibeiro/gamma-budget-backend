from abc import ABCMeta, abstractmethod

from budget.domain.entities.limit import Limit


class AbstractLimitUseCase(metaclass=ABCMeta):
    """Base class for use cases limit output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractLimitCreateUseCase(metaclass=ABCMeta):
    """Base class for use cases create limit output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractLimitListUseCase(metaclass=ABCMeta):
    """Base class for use cases list limits output."""

    @property
    @abstractmethod
    def execute(self) -> list[Limit]:
        pass


class AbstractLimitUpdateUseCase(metaclass=ABCMeta):
    """Base class for use cases update limit output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractLimitDeleteUseCase(metaclass=ABCMeta):
    """Base class for use cases delete limit output."""

    @property
    @abstractmethod
    def execute(self):
        pass
