from budget.data_access.incoming import (
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
    data_access: AbstractBaseIncomingCreateDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(
        self,
        user_id: int,
        data: dict,
        name: str,
        description: str,
        amount: float,
        category: str,
    ):
        super().__init__()
        self.user_id = user_id
        self.data = {
            "name": name,
            "description": description,
            "amount": amount,
            "category": category,
        }

    def execute(self, *args, **kwargs):
        incoming = self.data_access().create_incoming(data=self.data, user_id=self.user_id)
        if not incoming:
            raise Exception("Incoming not created, an error occurred.")
        parsed_incoming = incoming.to_dict()
        return self._build_output(parsed_incoming)

    def _build_output(self, incoming: dict):
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
    """
    Use case to list all incomings.
    """

    data_access: AbstractBaseIncomingListDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.result = []

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
    data_access: AbstractBaseIncomingRetrieveDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int, incoming_id: int):
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id
        self.result = []

    def execute(self):
        incoming = self.data_access().get_incoming(incoming_id=self.incoming_id, user_id=self.user_id)
        if not incoming:
            raise Exception("Incoming not found.")
        return self._build_output(incoming=incoming.to_dict())

    def _build_output(self, incoming: dict):
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
    data_access: AbstractBaseIncomingUpdateDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(
        self,
        user_id: int,
        incoming_id: int,
        data: dict,
    ):
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id
        self.data = data

    def execute(self):
        updated_incoming = self.data_access().update_incoming(
            user_id=self.user_id, incoming_id=self.incoming_id, data=self.data
        )
        if not updated_incoming:
            raise Exception("Incoming not updated.")
        incoming = updated_incoming.to_dict()
        return self._build_output(incoming=incoming)

    def _build_output(self, incoming: dict):
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
    data_access: AbstractBaseIncomingDeleteDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int, incoming_id: int):
        super().__init__()
        self.user_id = user_id
        self.incoming_id = incoming_id

    def execute(self):
        incoming = self.data_access().delete_incoming(self.user_id, self.incoming_id)
        return self._build_output(incoming=incoming)

    def _build_output(self, incoming):
        self.output = self.get_output_response()
        if not incoming:
            self.output.data = {"message": "Incoming not found."}
            return self.output
        self.output.data = {"message": "Incoming deleted successfully."}
        return self.output
