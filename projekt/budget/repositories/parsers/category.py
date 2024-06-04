from budget.domain.entities import Category
from budget.models import IncomingCategory, RevenueCategory


def parse_incoming_category_model_to_entity(incoming: IncomingCategory) -> Category:
    return Category(
        id=incoming.id,
        name=incoming.name,
        description=incoming.description,
    )


def parse_revenue_category_model_to_entity(revenue: RevenueCategory) -> Category:
    return Category(
        id=revenue.id,
        name=revenue.name,
        description=revenue.description,
    )
