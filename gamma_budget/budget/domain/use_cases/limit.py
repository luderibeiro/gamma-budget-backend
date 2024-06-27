from typing import Any

from budget.domain.data_access.limit import (
    AbstractBaseLimitCreateDataAccess,
    AbstractBaseLimitDeleteDataAccess,
    AbstractBaseLimitListDataAccess,
    AbstractBaseLimitUpdateDataAccess,
)
from budget.domain.use_cases.base import (
    AbstractBaseOutput,
    AbstractLimitCreateUseCase,
    AbstractLimitDeleteUseCase,
    AbstractLimitListUseCase,
    AbstractLimitUpdateUseCase,
)
from budget.domain.use_cases.features import (
    GetDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateDataAccessUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
)


class LimitCreateUseCase(
    AbstractLimitCreateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseLimitCreateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for creating limit budget records.

    Extends:
        AbstractLimitCreateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseLimitCreateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseLimitCreateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        data: dict,
        limit: float,
        limit_date: Any,
        amount: float,
        category: str,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            data (dict): The data for creating the limit record.
            amount (float): The amount of the limit record.
            category (str): The category of the limit record.
        """
        super().__init__()
        self.user_id = user_id
        self.data = {
            "limit": limit,
            "limit_date": limit_date,
            "amount": amount,
            "category": category,
        }

    def execute(self, *args, **kwargs):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        limit = self.data_access().create_limit(data=self.data, user_id=self.user_id)
        if not limit:
            return self._build_output(limit={"message": "Category not found."})
        parsed_limit = limit.to_dict()
        return self._build_output(parsed_limit)

    def _build_output(self, limit: dict):
        """
        Build the output response.

        Args:
        ----
            limit (dict): The limit data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = limit
        return self.output


class LimitListUseCase(
    AbstractLimitListUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseLimitListDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """Use case to list all limits."""

    data_access: type[AbstractBaseLimitListDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.result: list[dict] = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        limits = self.data_access().get_limits(self.user_id)
        if not limits:
            return self._build_output()
        for limit in limits:
            self.result.append(limit.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output


class LimitUpdateUseCase(
    AbstractLimitUpdateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseLimitUpdateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for updating an existing limit budget record.

    Extends:
        AbstractLimitUpdateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseLimitUpdateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseLimitUpdateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        limit_id: int,
        data: dict,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            limit_id (int): The ID of the limit record.
            data (dict): The updated data for the limit record.
        """
        super().__init__()
        self.user_id = user_id
        self.limit_id = limit_id
        self.data = data

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        updated_limit = self.data_access().update_limit(user_id=self.user_id, limit_id=self.limit_id, data=self.data)
        if not updated_limit:
            return self._build_output(limit={"message": "Limit not found."})
        limit = updated_limit.to_dict()
        return self._build_output(limit=limit)

    def _build_output(self, limit: dict):
        """
        Build the output response.

        Args:
        ----
            limit (dict): The limit data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = limit
        return self.output


class LimitDeleteUseCase(
    AbstractLimitDeleteUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseLimitDeleteDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for deleting an existing limit budget record.

    Extends:
        AbstractLimitDeleteUseCase
        GetDataAccessUseCaseMixin[AbstractBaseLimitDeleteDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseLimitDeleteDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int, limit_id: int):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            limit_id (int): The ID of the limit record to be deleted.
        """
        super().__init__()
        self.user_id = user_id
        self.limit_id = limit_id

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        limit = self.data_access().delete_limit(self.user_id, self.limit_id)
        return self._build_output(limit=limit)

    def _build_output(self, limit):
        """
        Build the output response.

        Args:
        ----
            limit: The limit record.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        if not limit:
            self.output.data = {"message": "Limit not found."}
            return self.output
        self.output.data = {"message": "Limit deleted successfully."}
        return self.output
