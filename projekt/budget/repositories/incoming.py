from typing import List

from budget.domain.data_access.incoming import (
    AbstractBaseIncomingCreateDataAccess,
    AbstractBaseIncomingDeleteDataAccess,
    AbstractBaseIncomingListDataAccess,
    AbstractBaseIncomingRetrieveDataAccess,
    AbstractBaseIncomingUpdateDataAccess,
)
from budget.domain.entities import Incoming
from budget.models import Incoming as IncomingModel
from budget.models.categories import IncomingCategory
from budget.repositories.parsers.incoming import parse_incoming_model_to_entity


class IncomingCreateRepository(AbstractBaseIncomingCreateDataAccess):
    def create_incoming(self, data: dict, user_id: int) -> Incoming:
        category = IncomingCategory.objects.get(id=data["category"])
        if not category:
            raise Exception("Category not found")
        incoming = IncomingModel.objects.create(
            user_id=user_id,
            name=data["name"],
            description=data["description"],
            amount=data["amount"],
            category=category,
        )
        return parse_incoming_model_to_entity(incoming)


class IncomingListRepository(AbstractBaseIncomingListDataAccess):
    def get_incomings(self, user_id) -> List[Incoming]:
        incoming_qs = IncomingModel.objects.all().filter(user_id=user_id)
        if not incoming_qs.exists():
            return None
        lista = [parse_incoming_model_to_entity(incoming) for incoming in incoming_qs.iterator()]
        return lista


class IncomingRetrieveRepository(AbstractBaseIncomingRetrieveDataAccess):
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        incoming = IncomingModel.objects.filter(id=incoming_id, user_id=user_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming.first())


class IncomingUpdateRepository(AbstractBaseIncomingUpdateDataAccess):
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        incoming = IncomingModel.objects.filter(id=incoming_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming)

    def update_incoming(self, user_id: int, incoming_id: str, data: dict) -> Incoming:
        incoming = IncomingModel.objects.filter(id=incoming_id, user_id=user_id).first()
        if not incoming:
            raise Exception("Incoming not found")
        incoming.name = data.get("name") if data.get("name") else incoming.name
        incoming.description = data.get("description") if data.get("description") else incoming.description
        incoming.amount = data.get("amount") if data.get("amount") else incoming.amount
        incoming.category = data.get("category") if data.get("category") else incoming.category
        incoming.save()
        return parse_incoming_model_to_entity(incoming)


class IncomingDeleteRepository(AbstractBaseIncomingDeleteDataAccess):
    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming:
        incoming = IncomingModel.objects.filter(id=incoming_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming)

    def delete_incoming(self, user_id: int, incoming_id: str) -> bool:
        incoming = IncomingModel.objects.filter(user_id=user_id, id=incoming_id)
        if not incoming.exists():
            return False
        incoming.delete()
        return True
