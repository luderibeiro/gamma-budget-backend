from abc import ABCMeta, abstractmethod

from budget.domain.entities.limit import Limit


class AbstractBaseLimitCreateDataAccess(metaclass=ABCMeta):
    """Base class for limit create data access."""

    @abstractmethod
    def create_limit(self, data: dict, user_id: int) -> Limit | None:
        pass


class AbstractBaseLimitListDataAccess(metaclass=ABCMeta):
    """Base class for limit list data access."""

    @abstractmethod
    def get_limits(self, user_id: int) -> list[Limit] | None:
        pass


class AbstractBaseLimitUpdateDataAccess(metaclass=ABCMeta):
    """Base class for limit update data access."""

    @abstractmethod
    def get_limit(self, limit_id: int, user_id: int) -> Limit | None:
        pass

    @abstractmethod
    def update_limit(self, user_id: int, limit_id: str, data: dict) -> Limit | None:
        pass


class AbstractBaseLimitDeleteDataAccess(metaclass=ABCMeta):
    """Base class for limit delete data access."""

    @abstractmethod
    def get_limit(self, limit_id: int, user_id: int) -> Limit | None:
        pass

    @abstractmethod
    def delete_limit(self, user_id: int, limit_id: str) -> bool:
        pass
