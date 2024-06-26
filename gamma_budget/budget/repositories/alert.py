from budget.domain.data_access.alert import (
    AbstractBaseAlertCreateDataAccess,
    AbstractBaseAlertDeleteDataAccess,
    AbstractBaseAlertListDataAccess,
    AbstractBaseAlertUpdateDataAccess,
)
from budget.domain.entities import Alert
from budget.models import Alert as AlertModel
from budget.models.categories import RevenueCategory
from budget.models.revenue import Revenue
from budget.repositories.parsers.alert import parse_alert_model_to_entity


class AlertCreateRepository(AbstractBaseAlertCreateDataAccess):
    """Repository for creating Alert instances."""

    def create_alert(self, data: dict, user_id: int) -> Alert | None:
        """Create an Alert instance.

        Args:
        ----
            data (dict): The data for creating the Alert instance.
            user_id (int): The ID of the user creating the Alert instance.

        Returns:
        -------
            Alert | None: The created Alert instance, or None if creation failed.
        """
        alert = AlertModel.objects.create(
            user_id=user_id,
            user_email=data.get("user_email"),
            revenue_id=data.get("revenue_id"),
            message=data.get("message"),
            alert_date=data.get("alert_date"),
        )
        return parse_alert_model_to_entity(alert)


class AlertListRepository(AbstractBaseAlertListDataAccess):
    """Repository for listing Alert instances."""

    def get_alerts(self, user_id: int) -> list[Alert] | None:
        """Get a list of Alert instances for a user.

        Args:
        ----
            user_id (int): The ID of the user.

        Returns:
        -------
            list[Alert] | None: A list of Alert instances, or None if no instances found.
        """
        alert_qs = AlertModel.objects.all().filter(user_id=user_id)
        if not alert_qs.exists():
            return None
        lista = [parse_alert_model_to_entity(alert) for alert in alert_qs.iterator()]
        return lista


class AlertUpdateRepository(AbstractBaseAlertUpdateDataAccess):
    """Repository for updating an Alert instance."""

    def get_alert(self, alert_id: int, user_id: int) -> Alert | None:
        """Retrieve an Alert instance by its ID and user ID.

        Args:
        ----
            alert_id (int): The ID of the Alert instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Alert | None: The retrieved Alert instance, or None if not found.
        """
        alert = AlertModel.objects.filter(id=alert_id)
        if not alert.exists():
            return None
        return parse_alert_model_to_entity(alert)

    def update_alert(self, user_id: int, alert_id: str, data: dict) -> Alert | None:
        """Update an Alert instance.

        Args:
        ----
            user_id (int): The ID of the user.
            alert_id (str): The ID of the Alert instance.
            data (dict): The data for updating the Alert instance.

        Returns:
        -------
            Alert | None: The updated Alert instance, or None if update failed.
        """
        revenue = Revenue.objects.get(id=data.get("revenue_id")) if data.get("revenue_id") else None
        alert = AlertModel.objects.filter(id=alert_id, user_id=user_id).first()
        if not alert:
            return None
        alert.revenue = revenue if revenue else alert.revenue
        alert.user_email = data.get("user_email") if data.get("user_email") else alert.user_email
        alert.message = data.get("message") if data.get("message") else alert.message
        alert.alert_date = data.get("alert_date") if data.get("alert_date") else alert.alert_date
        alert.save()
        return parse_alert_model_to_entity(alert)


class AlertDeleteRepository(AbstractBaseAlertDeleteDataAccess):
    """Repository for deleting an Alert instance."""

    def get_alert(self, alert_id: int, user_id: int) -> Alert | None:
        """Retrieve an Alert instance by its ID and user ID.

        Args:
        ----
            alert_id (int): The ID of the Alert instance.
            user_id (int): The ID of the user.

        Returns:
        -------
            Alert | None: The retrieved Alert instance, or None if not found.
        """
        alert = AlertModel.objects.filter(id=alert_id)
        if not alert.exists():
            return None
        return parse_alert_model_to_entity(alert)

    def delete_alert(self, user_id: int, alert_id: str) -> bool:
        """Delete an Alert instance by its ID and user ID.

        Args:
        ----
            user_id (int): The ID of the user.
            alert_id (str): The ID of the Alert instance.

        Returns:
        -------
            bool: True if the Alert instance was deleted, False otherwise.
        """
        alert = AlertModel.objects.filter(user_id=user_id, id=alert_id)
        if not alert.exists():
            return False
        alert.delete()
        return True
