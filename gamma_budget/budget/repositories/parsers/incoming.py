from budget.domain.entities import Incoming
from budget.models import Incoming as IncomingModel


def parse_incoming_model_to_entity(incoming: IncomingModel) -> Incoming:
    return Incoming(
        id=incoming.id,
        user_id=incoming.user_id,
        name=incoming.name,
        description=incoming.description,
        amount=incoming.amount,
        launch_date=incoming.launch_date,
        incoming_date=incoming.incoming_date,
        category={
            "id": incoming.category.id,
            "name": incoming.category.name,
        },
    )
