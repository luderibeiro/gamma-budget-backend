from budget.domain.entities import Revenue
from budget.models import Revenue as RevenueModel


def parse_revenue_model_to_entity(revenue: RevenueModel) -> Revenue:
    return Revenue(
        id=revenue.id,
        user_id=revenue.user_id,
        name=revenue.name,
        description=revenue.description,
        amount=revenue.amount,
        expiration_date=revenue.expiration_date,
        paid=revenue.paid,
        payment_date=revenue.payment_date if revenue.paid else None,
        category={
            "id": revenue.category.id,
            "name": revenue.category.name,
        },
    )
