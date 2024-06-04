from abc import ABCMeta, abstractmethod


class AbstractIncomingCategoryUseCase(metaclass=ABCMeta):
    """Base class for use cases incoming category output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractIncomingCategoryListUseCase(metaclass=ABCMeta):
    """Base class for use cases list incoming categories output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueCategoryUseCase(metaclass=ABCMeta):
    """Base class for use cases revenue category output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueCategoryListUseCase(metaclass=ABCMeta):
    """Base class for use cases list revenue categories output."""

    @property
    @abstractmethod
    def execute(self):
        pass
