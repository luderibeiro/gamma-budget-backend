from budget.domain.entities import Incoming
from budget.models import Incoming as IncomingModel


def parse_incoming_model_to_entity(incoming: IncomingModel) -> Incoming:
    return Incoming(
        name=incoming.name,
        description=incoming.description,
        amount=incoming.amount,
        launch_date=incoming.launch_date,
        category=incoming.category.name,
    )
