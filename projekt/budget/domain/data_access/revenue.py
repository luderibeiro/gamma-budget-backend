from abc import ABCMeta, abstractmethod
from typing import List

from budget.domain.entities.revenue import Revenue


class AbstractBaseRevenueCreateDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue create data access.
    """

    @abstractmethod
    def create_revenue(self, user_id: int) -> Revenue:
        pass


class AbstractBaseRevenueListDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue list data access.
    """

    @abstractmethod
    def get_revenues(self, user_id: int) -> List[Revenue]:
        pass


class AbstractBaseRevenueRetrieveDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue retrieve data access.
    """

    @abstractmethod
    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue:
        pass


class AbstractBaseRevenueUpdateDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue update data access.
    """

    @abstractmethod
    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue:
        pass

    @abstractmethod
    def update_revenue(self, user_id: int, revenue_id: str, data: dict) -> Revenue:
        pass


class AbstractBaseRevenueDeleteDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue delete data access.
    """

    @abstractmethod
    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue:
        pass

    @abstractmethod
    def delete_revenue(self, user_id: int, revenue_id: str) -> bool:
        pass
