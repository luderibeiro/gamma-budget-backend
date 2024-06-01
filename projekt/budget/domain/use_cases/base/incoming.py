from abc import ABCMeta, abstractmethod
from typing import List

from budget.domain.entities.incoming import Incoming


class AbstractIncomingUseCase(metaclass=ABCMeta):
    """
    Base class for use cases incoming output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractIncomingCreateUseCase(metaclass=ABCMeta):
    """
    Base class for use cases create incoming output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractIncomingListUseCase(metaclass=ABCMeta):
    """
    Base class for use cases list incomings output.
    """

    @property
    @abstractmethod
    def execute(self) -> List[Incoming]:
        pass


class AbstractIncomingRetrieveUseCase(metaclass=ABCMeta):
    """
    Base class for use cases retrieve incoming output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractIncomingUpdateUseCase(metaclass=ABCMeta):
    """
    Base class for use cases update incoming output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractIncomingDeleteUseCase(metaclass=ABCMeta):
    """
    Base class for use cases delete incoming output.
    """

    @property
    @abstractmethod
    def execute(self):
        pass
