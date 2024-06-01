from abc import ABCMeta, abstractmethod

from budget.domain.entities.incoming import Incoming


class AbstractBaseIncomingCreateDataAccess(metaclass=ABCMeta):
    """Base class for incoming create data access."""

    @abstractmethod
    def create_incoming(self, user_id: int) -> Incoming:
        pass


class AbstractBaseIncomingListDataAccess(metaclass=ABCMeta):
    """Base class for incoming list data access."""

    @abstractmethod
    def get_incomings(self, user_id: int) -> list[Incoming]:
        pass


class AbstractBaseIncomingRetrieveDataAccess(metaclass=ABCMeta):
    """Base class for incoming retrieve data access."""

    @abstractmethod
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        pass


class AbstractBaseIncomingUpdateDataAccess(metaclass=ABCMeta):
    """Base class for incoming update data access."""

    @abstractmethod
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        pass

    @abstractmethod
    def update_incoming(self, user_id: int, incoming_id: str, data: dict) -> Incoming:
        pass


class AbstractBaseIncomingDeleteDataAccess(metaclass=ABCMeta):
    """Base class for incoming delete data access."""

    @abstractmethod
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        pass

    @abstractmethod
    def delete_incoming(self, user_id: int, incoming_id: str) -> bool:
        pass
