from budget.domain.data_access.limit import (
    AbstractBaseLimitCreateDataAccess,
    AbstractBaseLimitDeleteDataAccess,
    AbstractBaseLimitListDataAccess,
    AbstractBaseLimitUpdateDataAccess,
)
from budget.domain.entities import Limit
from budget.models import Limit as LimitModel
from budget.models.categories import RevenueCategory
from budget.repositories.parsers.limit import parse_limit_model_to_entity


class LimitCreateRepository(AbstractBaseLimitCreateDataAccess):
    """Repository for creating Limit instances."""

    def create_limit(self, data: dict, user_id: int) -> Limit | None:
        """Create an Limit instance.

        Args:
        ----
            data (dict): The data for creating the Limit instance.
            user_id (int): The ID of the user creating the Limit instance.

        Returns:
        -------
            Limit | None: The created Limit instance, or None if creation failed.
        """
        category = RevenueCategory.objects.get(id=data["category"])
        if not category:
            return None
        limit = LimitModel.objects.create(
            user_id=user_id,
            limit=data.get("limit"),
            limit_date=data.get("limit_date"),
            amount=data.get("amount"),
            category=category,
        )
        return parse_limit_model_to_entity(limit)


class LimitListRepository(AbstractBaseLimitListDataAccess):
    """Repository for listing Limit instances."""

    def get_limits(self, user_id: int) -> list[Limit] | None:
        """Get a list of Limit instances for a user.

        Args:
        ----
            user_id (int): The ID of the user.

        Returns:
        -------
            list[Limit] | None: A list of Limit instances, or None if no instances found.
        """
        limit_qs = LimitModel.objects.all().filter(user_id=user_id)
        print("LIMITS", limit_qs)
        if not limit_qs.exists():
            return None
        lista = [parse_limit_model_to_entity(limit) for limit in limit_qs.iterator()]
        return lista


class LimitUpdateRepository(AbstractBaseLimitUpdateDataAccess):
    """Repository for updating an Limit instance."""

    def get_limit(self, limit_id: int, user_id: int) -> Limit | None:
        """Retrieve an Limit instance by its ID and user ID.

        Args:
        ----
            limit_id (int): The ID of the Limit instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Limit | None: The retrieved Limit instance, or None if not found.
        """
        limit = LimitModel.objects.filter(id=limit_id)
        if not limit.exists():
            return None
        return parse_limit_model_to_entity(limit)

    def update_limit(self, user_id: int, limit_id: str, data: dict) -> Limit | None:
        """Update an Limit instance.

        Args:
        ----
            user_id (int): The ID of the user.
            limit_id (str): The ID of the Limit instance.
            data (dict): The data for updating the Limit instance.

        Returns:
        -------
            Limit | None: The updated Limit instance, or None if update failed.
        """
        limit = LimitModel.objects.filter(id=limit_id, user_id=user_id).first()
        limit.limit = data.get("limit") if data.get("limit") else limit.limit
        limit.amount = data.get("amount") if data.get("amount") else limit.amount
        limit.save()
        return parse_limit_model_to_entity(limit)


class LimitDeleteRepository(AbstractBaseLimitDeleteDataAccess):
    """Repository for deleting an Limit instance."""

    def get_limit(self, limit_id: int, user_id: int) -> Limit | None:
        """Retrieve an Limit instance by its ID and user ID.

        Args:
        ----
            limit_id (int): The ID of the Limit instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Limit | None: The retrieved Limit instance, or None if not found.
        """
        limit = LimitModel.objects.filter(id=limit_id)
        if not limit.exists():
            return None
        return parse_limit_model_to_entity(limit)

    def delete_limit(self, user_id: int, limit_id: str) -> bool:
        """Delete an Limit instance by its ID and user ID.

        Args:
        ----
            user_id (int): The ID of the user.
            limit_id (str): The ID of the Limit instance.

        Returns:
        -------
            bool: True if the Limit instance was deleted, False otherwise.
        """
        limit = LimitModel.objects.filter(user_id=user_id, id=limit_id)
        if not limit.exists():
            return False
        limit.delete()
        return True
