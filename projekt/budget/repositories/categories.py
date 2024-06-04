from typing import List

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
    def get_incoming_categories(self) -> List[Category]:
        incoming_categories_qs = IncomingCategory.objects.all()
        if not incoming_categories_qs.exists():
            return None
        lista = [
            parse_incoming_category_model_to_entity(category)
            for category in incoming_categories_qs.iterator()
        ]
        return lista


class RevenueCategoryListRepository(AbstractBaseRevenueCategoryListDataAccess):
    def get_revenue_categories(self) -> List[Category]:
        revenue_categories_qs = RevenueCategory.objects.all()
        if not revenue_categories_qs.exists():
            return None
        lista = [
            parse_revenue_category_model_to_entity(category) for category in revenue_categories_qs.iterator()
        ]
        return lista
