from abc import ABCMeta, abstractmethod

from budget.domain.entities.alert import Alert


class AbstractAlertUseCase(metaclass=ABCMeta):
    """Base class for use cases alert output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractAlertCreateUseCase(metaclass=ABCMeta):
    """Base class for use cases create alert output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractAlertListUseCase(metaclass=ABCMeta):
    """Base class for use cases list alerts output."""

    @property
    @abstractmethod
    def execute(self) -> list[Alert]:
        pass


class AbstractAlertUpdateUseCase(metaclass=ABCMeta):
    """Base class for use cases update alert output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractAlertDeleteUseCase(metaclass=ABCMeta):
    """Base class for use cases delete alert output."""

    @property
    @abstractmethod
    def execute(self):
        pass


class AbstractAlertSendEmailUseCase(metaclass=ABCMeta):
    """Base class for use cases send email alert output."""

    @property
    @abstractmethod
    def execute(self):
        pass
