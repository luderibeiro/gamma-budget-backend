from budget.domain.data_access.revenue import (
    AbstractBaseRevenueCreateDataAccess,
    AbstractBaseRevenueDeleteDataAccess,
    AbstractBaseRevenueListDataAccess,
    AbstractBaseRevenueRetrieveDataAccess,
    AbstractBaseRevenueUpdateDataAccess,
)
from budget.domain.use_cases.base import (
    AbstractBaseOutput,
    AbstractRevenueCreateUseCase,
    AbstractRevenueDeleteUseCase,
    AbstractRevenueListUseCase,
    AbstractRevenueRetrieveUseCase,
    AbstractRevenueUpdateUseCase,
)
from budget.domain.use_cases.features import (
    GetDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateDataAccessUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
)


class RevenueCreateUseCase(
    AbstractRevenueCreateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseRevenueCreateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    data_access: AbstractBaseRevenueCreateDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(
        self,
        user_id: int,
        data: dict,
        name: str,
        description: str,
        amount: float,
        expiration_date: str,
        paid: bool,
        payment_date: str,
        category: str,
    ):
        super().__init__()
        self.user_id = user_id
        self.data = {
            "name": name,
            "description": description,
            "amount": amount,
            "expiration_date": expiration_date,
            "paid": paid,
            "payment_date": payment_date if paid else None,
            "category": category,
        }

    def execute(self, *args, **kwargs):
        try:
            revenue = self.data_access().create_revenue(data=self.data, user_id=self.user_id)
        except Exception as e:
            return self._build_output(revenue={"message": str(e)})
        parsed_revenue = revenue.to_dict()
        return self._build_output(parsed_revenue)

    def _build_output(self, revenue: dict):
        self.output = self.get_output_response()
        self.output.data = revenue
        return self.output


class RevenueListUseCase(
    AbstractRevenueListUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseRevenueListDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    """
    Use case to list all revenues.
    """

    data_access: AbstractBaseRevenueListDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.result = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        revenues = self.data_access().get_revenues(self.user_id)
        if not revenues:
            return self._build_output()
        for revenue in revenues:
            self.result.append(revenue.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output


class RevenueRetrieveUseCase(
    AbstractRevenueRetrieveUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseRevenueRetrieveDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    data_access: AbstractBaseRevenueRetrieveDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int, revenue_id: int):
        super().__init__()
        self.user_id = user_id
        self.revenue_id = revenue_id
        self.result = []

    def execute(self):
        try:
            revenue = self.data_access().get_revenue(revenue_id=self.revenue_id, user_id=self.user_id)
        except Exception as e:
            return self._build_output(revenue={"message": str(e)})
        return self._build_output(revenue=revenue.to_dict())

    def _build_output(self, revenue: dict):
        self.output = self.get_output_response()
        self.output.data = revenue
        return self.output


class RevenueUpdateUseCase(
    AbstractRevenueUpdateUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseRevenueUpdateDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    data_access: AbstractBaseRevenueUpdateDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(
        self,
        user_id: int,
        revenue_id: int,
        data: dict,
    ):
        super().__init__()
        self.user_id = user_id
        self.revenue_id = revenue_id
        self.data = data

    def execute(self):
        updated_revenue = self.data_access().update_revenue(
            user_id=self.user_id, revenue_id=self.revenue_id, data=self.data
        )
        if not updated_revenue:
            return self._build_output(revenue={"message": "Revenue not found."})
        revenue = updated_revenue.to_dict()
        return self._build_output(revenue=revenue)

    def _build_output(self, revenue: dict):
        self.output = self.get_output_response()
        self.output.data = revenue
        return self.output


class RevenueDeleteUseCase(
    AbstractRevenueDeleteUseCase,
    GetDataAccessUseCaseMixin[AbstractBaseRevenueDeleteDataAccess],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):
    data_access: AbstractBaseRevenueDeleteDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self, user_id: int, revenue_id: int):
        super().__init__()
        self.user_id = user_id
        self.revenue_id = revenue_id

    def execute(self):
        revenue = self.data_access().delete_revenue(self.user_id, self.revenue_id)
        return self._build_output(revenue=revenue)

    def _build_output(self, revenue):
        self.output = self.get_output_response()
        if not revenue:
            self.output.data = {"message": "Revenue not found."}
            return self.output
        self.output.data = {"message": "Revenue deleted successfully."}
        return self.output