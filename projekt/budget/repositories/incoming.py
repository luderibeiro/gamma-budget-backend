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
    """Repository for creating Incoming instances."""

    def create_incoming(self, data: dict, user_id: int) -> Incoming | None:
        """Create an Incoming instance.

        Args:
        ----
            data (dict): The data for creating the Incoming instance.
            user_id (int): The ID of the user creating the Incoming instance.

        Returns:
        -------
            Incoming | None: The created Incoming instance, or None if creation failed.
        """
        category = IncomingCategory.objects.get(id=data["category"])
        if not category:
            return None
        incoming = IncomingModel.objects.create(
            user_id=user_id,
            name=data["name"],
            description=data["description"],
            amount=data["amount"],
            category=category,
        )
        return parse_incoming_model_to_entity(incoming)


class IncomingListRepository(AbstractBaseIncomingListDataAccess):
    """Repository for listing Incoming instances."""

    def get_incomings(self, user_id: int) -> list[Incoming] | None:
        """Get a list of Incoming instances for a user.

        Args:
        ----
            user_id (int): The ID of the user.

        Returns:
        -------
            list[Incoming] | None: A list of Incoming instances, or None if no instances found.
        """
        incoming_qs = IncomingModel.objects.all().filter(user_id=user_id)
        if not incoming_qs.exists():
            return None
        lista = [
            parse_incoming_model_to_entity(incoming)
            for incoming in incoming_qs.iterator()
        ]
        return lista


class IncomingRetrieveRepository(AbstractBaseIncomingRetrieveDataAccess):
    """Repository for retrieving an Incoming instance."""

    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming | None:
        """Retrieve an Incoming instance by its ID and user ID.

        Args:
        ----
            incoming_id (int): The ID of the Incoming instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Incoming | None: The retrieved Incoming instance, or None if not found.
        """
        incoming = IncomingModel.objects.filter(id=incoming_id, user_id=user_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming.first())


class IncomingUpdateRepository(AbstractBaseIncomingUpdateDataAccess):
    """Repository for updating an Incoming instance."""

    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming | None:
        """Retrieve an Incoming instance by its ID and user ID.

        Args:
        ----
            incoming_id (int): The ID of the Incoming instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Incoming | None: The retrieved Incoming instance, or None if not found.
        """
        incoming = IncomingModel.objects.filter(id=incoming_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming)

    def update_incoming(
        self, user_id: int, incoming_id: str, data: dict
    ) -> Incoming | None:
        """Update an Incoming instance.

        Args:
        ----
            user_id (int): The ID of the user.
            incoming_id (str): The ID of the Incoming instance.
            data (dict): The data for updating the Incoming instance.

        Returns:
        -------
            Incoming | None: The updated Incoming instance, or None if update failed.
        """
        incoming = IncomingModel.objects.filter(id=incoming_id, user_id=user_id).first()
        category = (
            IncomingCategory.objects.get(id=data["category"])
            if data.get("category")
            else None
        )
        if not incoming:
            return None
        incoming.name = data.get("name") if data.get("name") else incoming.name
        incoming.description = (
            data.get("description") if data.get("description") else incoming.description
        )
        incoming.amount = data.get("amount") if data.get("amount") else incoming.amount
        incoming.category = category if category else incoming.category
        incoming.save()
        return parse_incoming_model_to_entity(incoming)


class IncomingDeleteRepository(AbstractBaseIncomingDeleteDataAccess):
    """Repository for deleting an Incoming instance."""

    def get_incoming(self, incoming_id: int, user_id: int) -> Incoming | None:
        """Retrieve an Incoming instance by its ID and user ID.

        Args:
        ----
            incoming_id (int): The ID of the Incoming instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Incoming | None: The retrieved Incoming instance, or None if not found.
        """
        incoming = IncomingModel.objects.filter(id=incoming_id)
        if not incoming.exists():
            return None
        return parse_incoming_model_to_entity(incoming)

    def delete_incoming(self, user_id: int, incoming_id: str) -> bool:
        """Delete an Incoming instance by its ID and user ID.

        Args:
        ----
            user_id (int): The ID of the user.
            incoming_id (str): The ID of the Incoming instance.

        Returns:
        -------
            bool: True if the Incoming instance was deleted, False otherwise.
        """
        incoming = IncomingModel.objects.filter(user_id=user_id, id=incoming_id)
        if not incoming.exists():
            return False
        incoming.delete()
        return True
