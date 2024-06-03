from budget.domain.data_access.revenue import (
    AbstractBaseRevenueCreateDataAccess,
    AbstractBaseRevenueDeleteDataAccess,
    AbstractBaseRevenueListDataAccess,
    AbstractBaseRevenueRetrieveDataAccess,
    AbstractBaseRevenueUpdateDataAccess,
)
from budget.domain.entities import Revenue
from budget.models import Revenue as RevenueModel
from budget.models.categories import RevenueCategory
from budget.repositories.parsers.revenue import parse_revenue_model_to_entity


class RevenueCreateRepository(AbstractBaseRevenueCreateDataAccess):
    """Repository for creating Revenue instances.

    Args:
    ----
        AbstractBaseRevenueCreateDataAccess: Abstract base class for creating Revenue instances.
    """

    def create_revenue(self, data: dict, user_id: int) -> Revenue | None:
        """Create a revenue instance.

        Args:
        ----
            data (dict): Data for creating the revenue.
            user_id (int): User ID associated with the revenue.

        Returns:
        -------
            Revenue | None: Created Revenue instance or None if creation fails.
        """
        category = RevenueCategory.objects.get(id=data["category"])
        print("expiration_date", data.get("expiration_date"))
        if not category:
            return None
        revenue = RevenueModel.objects.create(
            user_id=user_id,
            name=data.get("name"),
            description=data.get("description"),
            amount=data.get("amount"),
            expiration_date=data.get("expiration_date"),
            paid=data.get("paid"),
            payment_date=data.get("payment_date"),
            category=category,
        )
        return parse_revenue_model_to_entity(revenue)


class RevenueListRepository(AbstractBaseRevenueListDataAccess):
    """Repository for listing Revenue instances.

    Args:
    ----
        AbstractBaseRevenueListDataAccess: Abstract base class for listing Revenue instances.
    """

    def get_revenues(self, user_id) -> list[Revenue] | None:
        """Get a list of revenue instances.

        Args:
        ----
            user_id: User ID associated with the revenues.

        Returns:
        -------
            list[Revenue] | None: List of Revenue instances or None if no revenues found.
        """
        revenue_qs = RevenueModel.objects.all().filter(user_id=user_id)
        if not revenue_qs.exists():
            return None
        lista = [
            parse_revenue_model_to_entity(revenue) for revenue in revenue_qs.iterator()
        ]
        return lista


class RevenueRetrieveRepository(AbstractBaseRevenueRetrieveDataAccess):
    """Repository for retrieving a single Revenue instance.

    Args:
    ----
        AbstractBaseRevenueRetrieveDataAccess: Abstract base class for retrieving a single Revenue instance.
    """

    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue | None:
        """Get a single revenue instance.

        Args:
        ----
            revenue_id (int): ID of the revenue to retrieve.
            user_id (int): User ID associated with the revenue.

        Returns:
        -------
            Revenue | None: Retrieved Revenue instance or None if not found.
        """
        revenue = RevenueModel.objects.filter(id=revenue_id, user_id=user_id)
        if not revenue.exists():
            return None
        return parse_revenue_model_to_entity(revenue.first())


class RevenueUpdateRepository(AbstractBaseRevenueUpdateDataAccess):
    """Repository for updating Revenue instances.

    Args:
    ----
        AbstractBaseRevenueUpdateDataAccess: Abstract base class for updating Revenue instances.
    """

    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue | None:
        """Get a single revenue instance for update.

        Args:
        ----
            revenue_id (int): ID of the revenue to update.
            user_id (int): User ID associated with the revenue.

        Returns:
        -------
            Revenue | None: Retrieved Revenue instance for update or None if not found.
        """
        revenue = RevenueModel.objects.filter(id=revenue_id)
        if not revenue.exists():
            return None
        return parse_revenue_model_to_entity(revenue)

    def update_revenue(
        self, user_id: int, revenue_id: str, data: dict
    ) -> Revenue | None:
        """Update a revenue instance.

        Args:
        ----
            user_id (int): User ID associated with the revenue.
            revenue_id (str): ID of the revenue to update.
            data (dict): Updated data for the revenue.

        Returns:
        -------
            Revenue | None: Updated Revenue instance or None if update fails.
        """
        revenue = RevenueModel.objects.filter(id=revenue_id, user_id=user_id).first()
        category = (
            RevenueCategory.objects.get(id=data["category"])
            if data.get("category")
            else None
        )
        if not revenue:
            return None
        revenue.name = data.get("name") if data.get("name") else revenue.name
        revenue.description = (
            data.get("description") if data.get("description") else revenue.description
        )
        revenue.amount = data.get("amount") if data.get("amount") else revenue.amount
        revenue.expiration_date = (
            data.get("expiration_date")
            if data.get("expiration_date")
            else revenue.expiration_date
        )
        revenue.paid = data.get("paid")
        revenue.payment_date = (
            data.get("payment_date")
            if data.get("payment_date")
            else revenue.payment_date
        )
        revenue.category = category if category else revenue.category
        revenue.save()
        return parse_revenue_model_to_entity(revenue)


class RevenueDeleteRepository(AbstractBaseRevenueDeleteDataAccess):
    """Repository for deleting Revenue instances.

    Args:
    ----
        AbstractBaseRevenueDeleteDataAccess: Abstract base class for deleting Revenue instances.
    """

    def get_revenue(self, revenue_id: int, user_id: int) -> Revenue | None:
        """Get a single revenue instance for deletion.

        Args:
        ----
            revenue_id (int): ID of the revenue to delete.
            user_id (int): User ID associated with the revenue.

        Returns:
        -------
            Revenue | None: Retrieved Revenue instance for deletion or None if not found.
        """
        revenue = RevenueModel.objects.filter(id=revenue_id)
        if not revenue.exists():
            return None
        return parse_revenue_model_to_entity(revenue)

    def delete_revenue(self, user_id: int, revenue_id: str) -> bool:
        """Delete a revenue instance.

        Args:
        ----
            user_id (int): User ID associated with the revenue.
            revenue_id (str): ID of the revenue to delete.

        Returns:
        -------
            bool: True if deletion is successful, False otherwise.
        """
        revenue = RevenueModel.objects.filter(user_id=user_id, id=revenue_id)
        if not revenue.exists():
            return False
        revenue.delete()
        return True
