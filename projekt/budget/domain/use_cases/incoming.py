from typing import Any

from budget.domain.data_access.incoming import (
    AbstractBaseIncomingCreateDataAccess,
    AbstractBaseIncomingDeleteDataAccess,
    AbstractBaseIncomingListDataAccess,
    AbstractBaseIncomingRetrieveDataAccess,
    AbstractBaseIncomingUpdateDataAccess,
)
from budget.domain.use_cases.base import (
    AbstractBaseOutput,
    AbstractIncomingCreateUseCase,
    AbstractIncomingDeleteUseCase,
    AbstractIncomingListUseCase,
    AbstractIncomingRetrieveUseCase,
    AbstractIncomingUpdateUseCase,
)
from budget.domain.use_cases.features import (
    GetDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateDataAccessUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
)


class IncomingCreateUseCase(
    AbstractIncomingCreateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseIncomingCreateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for creating incoming budget records.

    Extends:
        AbstractIncomingCreateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseIncomingCreateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseIncomingCreateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        data: dict,
        name: str,
        description: str,
        amount: float,
        category: str,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            data (dict): The data for creating the incoming record.
            name (str): The name of the incoming record.
            description (str): The description of the incoming record.
            amount (float): The amount of the incoming record.
            category (str): The category of the incoming record.
        """
        super().__init__()
        self.user_id = user_id
        self.data = {
            "name": name,
            "description": description,
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
        incoming = self.data_access().create_incoming(
            data=self.data, user_id=self.user_id
        )
        if not incoming:
            return self._build_output(incoming={"message": "Category not found."})
        parsed_incoming = incoming.to_dict()
        return self._build_output(parsed_incoming)

    def _build_output(self, incoming: dict):
        """
        Build the output response.

        Args:
        ----
            incoming (dict): The incoming data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = incoming
        return self.output


class IncomingListUseCase(
    AbstractIncomingListUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseIncomingListDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """Use case to list all incomings."""

    data_access: type[AbstractBaseIncomingListDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.result: list[dict] = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        incomings = self.data_access().get_incomings(self.user_id)
        if not incomings:
            return self._build_output()
        for incoming in incomings:
            self.result.append(incoming.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output


class IncomingRetrieveUseCase(
    AbstractIncomingRetrieveUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseIncomingRetrieveDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for retrieving a specific incoming budget record.

    Extends:
        AbstractIncomingRetrieveUseCase
        GetDataAccessUseCaseMixin[AbstractBaseIncomingRetrieveDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseIncomingRetrieveDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int, incoming_id: int):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            incoming_id (int): The ID of the incoming record.
        """
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id
        self.result: list[Any] = []

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        incoming = self.data_access().get_incoming(
            incoming_id=self.incoming_id, user_id=self.user_id
        )
        if not incoming:
            return self._build_output(incoming={"message": "Incoming not found."})
        return self._build_output(incoming=incoming.to_dict())

    def _build_output(self, incoming: dict):
        """
        Build the output response.

        Args:
        ----
            incoming (dict): The incoming data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = incoming
        return self.output


class IncomingUpdateUseCase(
    AbstractIncomingUpdateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseIncomingUpdateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for updating an existing incoming budget record.

    Extends:
        AbstractIncomingUpdateUseCase
        GetDataAccessUseCaseMixin[AbstractBaseIncomingUpdateDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseIncomingUpdateDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(
        self,
        user_id: int,
        incoming_id: int,
        data: dict,
    ):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            incoming_id (int): The ID of the incoming record.
            data (dict): The updated data for the incoming record.
        """
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id
        self.data = data

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        updated_incoming = self.data_access().update_incoming(
            user_id=self.user_id, incoming_id=self.incoming_id, data=self.data
        )
        if not updated_incoming:
            return self._build_output(incoming={"message": "Incoming not found."})
        incoming = updated_incoming.to_dict()
        return self._build_output(incoming=incoming)

    def _build_output(self, incoming: dict):
        """
        Build the output response.

        Args:
        ----
            incoming (dict): The incoming data.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        self.output.data = incoming
        return self.output


class IncomingDeleteUseCase(
    AbstractIncomingDeleteUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseIncomingDeleteDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case for deleting an existing incoming budget record.

    Extends:
        AbstractIncomingDeleteUseCase
        GetDataAccessUseCaseMixin[AbstractBaseIncomingDeleteDataAccess]
        ValidateDataAccessUseCaseMixin
        GetOutputResponseUseCaseMixin
        ValidateOutputResponseUseCaseMixin
    """

    data_access: type[AbstractBaseIncomingDeleteDataAccess] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self, user_id: int, incoming_id: int):
        """
        Initialize the use case.

        Args:
        ----
            user_id (int): The ID of the user.
            incoming_id (int): The ID of the incoming record to be deleted.
        """
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id

    def execute(self):
        """
        Execute the use case.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        incoming = self.data_access().delete_incoming(self.user_id, self.incoming_id)
        return self._build_output(incoming=incoming)

    def _build_output(self, incoming):
        """
        Build the output response.

        Args:
        ----
            incoming: The incoming record.

        Returns:
        -------
            AbstractBaseOutput: The output response.
        """
        self.output = self.get_output_response()
        if not incoming:
            self.output.data = {"message": "Incoming not found."}
            return self.output
        self.output.data = {"message": "Incoming deleted successfully."}
        return self.output
