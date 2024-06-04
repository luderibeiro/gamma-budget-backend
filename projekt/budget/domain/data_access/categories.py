from abc import ABCMeta, abstractmethod
from typing import List

from budget.domain.entities.categories import Category


class AbstractBaseIncomingCategoryListDataAccess(metaclass=ABCMeta):
    """
    Base class for incoming category list data access.
    """

    @abstractmethod
    def get_incoming_categories(self) -> List[Category]:
        pass


class AbstractBaseRevenueCategoryListDataAccess(metaclass=ABCMeta):
    """
    Base class for revenue category list data access.
    """

    @abstractmethod
    def get_revenue_categories(self) -> List[Category]:
        pass
