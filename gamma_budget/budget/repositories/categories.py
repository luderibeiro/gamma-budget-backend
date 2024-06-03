from budget.domain.data_access.categories import (
    AbstractBaseIncomingCategoryListDataAccess,
    AbstractBaseRevenueCategoryListDataAccess,
)
from budget.domain.entities.categories import Category
from budget.models import IncomingCategory, RevenueCategory
from budget.repositories.parsers.category import (
    parse_incoming_category_model_to_entity,
    parse_revenue_category_model_to_entity,
)


class IncomingCategoryListRepository(AbstractBaseIncomingCategoryListDataAccess):
    """
    Repository for retrieving a list of IncomingCategory instances.

    This repository retrieves IncomingCategory instances from the database, converts them
    into Category entities, and returns the result as a list.

    Methods:
    -------
    get_incoming_categories() -> list[Category]
        Retrieves and returns a list of incoming category entities.
    """

    def get_incoming_categories(self) -> list[Category]:
        """
        Retrieves a list of IncomingCategory instances from the database.

        This method retrieves IncomingCategory instances from the database, converts them
        into Category entities, and returns the result as a list. If no instances are found,
        an empty list is returned.

        Returns:
        -------
        list[Category]
            A list of incoming category entities.
        """
        incoming_categories_qs = IncomingCategory.objects.all()
        if not incoming_categories_qs.exists():
            return []
        lista = [parse_incoming_category_model_to_entity(category) for category in incoming_categories_qs.iterator()]
        return lista


class RevenueCategoryListRepository(AbstractBaseRevenueCategoryListDataAccess):
    """
    Repository for retrieving a list of RevenueCategory instances.

    This repository retrieves RevenueCategory instances from the database, converts them
    into Category entities, and returns the result as a list.

    Methods:
    -------
    get_revenue_categories() -> list[Category]
        Retrieves and returns a list of revenue category entities.
    """

    def get_revenue_categories(self) -> list[Category]:
        """
        Retrieves a list of RevenueCategory instances from the database.

        This method retrieves RevenueCategory instances from the database, converts them
        into Category entities, and returns the result as a list. If no instances are found,
        an empty list is returned.

        Returns:
        -------
        list[Category]
            A list of revenue category entities.
        """
        revenue_categories_qs = RevenueCategory.objects.all()
        if not revenue_categories_qs.exists():
            return []
        lista = [parse_revenue_category_model_to_entity(category) for category in revenue_categories_qs.iterator()]
        return lista
