from abc import ABCMeta, abstractmethod
from typing import List

from budget.domain.entities.revenue import Revenue


class AbstractRevenueUseCase(metaclass=ABCMeta):
    """
    Base class for use cases revenue output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueCreateUseCase(metaclass=ABCMeta):
    """
    Base class for use cases create revenue output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueListUseCase(metaclass=ABCMeta):
    """
    Base class for use cases list revenues output.
    """

    @property
    @abstractmethod
    def execute(self) -> List[Revenue]:
        pass


class AbstractRevenueRetrieveUseCase(metaclass=ABCMeta):
    """
    Base class for use cases retrieve revenue output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueUpdateUseCase(metaclass=ABCMeta):
    """
    Base class for use cases update revenue output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractRevenueDeleteUseCase(metaclass=ABCMeta):
    """
    Base class for use cases delete revenue output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass
