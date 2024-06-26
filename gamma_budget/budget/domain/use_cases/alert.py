from typing import Any

from budget.domain.data_access.alert import (
    AbstractBaseAlertCreateDataAccess,
    AbstractBaseAlertDeleteDataAccess,
    AbstractBaseAlertListDataAccess,
    AbstractBaseAlertUpdateDataAccess,
)
from budget.domain.use_cases.base import (
    AbstractAlertCreateUseCase,
    AbstractAlertDeleteUseCase,
    AbstractAlertListUseCase,
    AbstractAlertUpdateUseCase,
    AbstractBaseOutput,
)
from budget.domain.use_cases.features import (
    GetDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateDataAccessUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
)


class AlertCreateUseCase(
    AbstractAlertCreateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseAlertCreateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for creating alert budget records.

    Extends:
        AbstractAlertCreateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseAlertCreateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseAlertCreateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        data: dict,
        user_email: str,
        revenue_id: str,
        message: str,
        alert_date: Any,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            data (dict): The data for creating the alert record.
            amount (float): The amount of the alert record.
            category (str): The category of the alert record.
        """
        super().__init__()
        self.user_id = user_id
        self.data = {
            "user_email": user_email,
            "revenue_id": revenue_id,
            "message": message,
            "alert_date": alert_date,
        }

    def execute(self, *args, **kwargs):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        alert = self.data_access().create_alert(data=self.data, user_id=self.user_id)
        if not alert:
            return self._build_output(alert={"message": "Category not found."})
        parsed_alert = alert.to_dict()
        _send_email(alert=parsed_alert)
        return self._build_output(parsed_alert)

    def _build_output(self, alert: dict):
        """
        Build the output response.

        Args:
        ----
            alert (dict): The alert data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = alert
        return self.output


class AlertListUseCase(
    AbstractAlertListUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseAlertListDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """Use case to list all alerts."""

    data_access: type[AbstractBaseAlertListDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.result: list[dict] = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        alerts = self.data_access().get_alerts(self.user_id)
        if not alerts:
            return self._build_output()
        for alert in alerts:
            self.result.append(alert.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output


class AlertUpdateUseCase(
    AbstractAlertUpdateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseAlertUpdateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for updating an existing alert budget record.

    Extends:
        AbstractAlertUpdateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseAlertUpdateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseAlertUpdateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        alert_id: int,
        data: dict,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            alert_id (int): The ID of the alert record.
            data (dict): The updated data for the alert record.
        """
        super().__init__()
        self.user_id = user_id
        self.alert_id = alert_id
        self.data = data

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        updated_alert = self.data_access().update_alert(user_id=self.user_id, alert_id=self.alert_id, data=self.data)
        if not updated_alert:
            return self._build_output(alert={"message": "Alert not found."})
        alert = updated_alert.to_dict()
        return self._build_output(alert=alert)

    def _build_output(self, alert: dict):
        """
        Build the output response.

        Args:
        ----
            alert (dict): The alert data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = alert
        return self.output


class AlertDeleteUseCase(
    AbstractAlertDeleteUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseAlertDeleteDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for deleting an existing alert budget record.

    Extends:
        AbstractAlertDeleteUseCase
        GetDataAccessUseCaseMixin[AbstractBaseAlertDeleteDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseAlertDeleteDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int, alert_id: int):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            alert_id (int): The ID of the alert record to be deleted.
        """
        super().__init__()
        self.user_id = user_id
        self.alert_id = alert_id

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        alert = self.data_access().delete_alert(self.user_id, self.alert_id)
        return self._build_output(alert=alert)

    def _build_output(self, alert):
        """
        Build the output response.

        Args:
        ----
            alert: The alert record.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        if not alert:
            self.output.data = {"message": "Alert not found."}
            return self.output
        self.output.data = {"message": "Alert deleted successfully."}
        return self.output
