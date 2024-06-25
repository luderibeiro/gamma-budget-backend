from budget.domain.entities import Limit
from budget.models import Limit as LimitModel


def parse_limit_model_to_entity(limit: LimitModel) -> Limit:
    return Limit(
        id=limit.id,
        user_id=limit.user_id,
        limit=limit.limit,
        amount=limit.amount,
        limit_date=limit.limit_date,
        category=limit.category.name,
    )
