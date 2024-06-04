from typing import List

from budget.domain.data_access.categories import (
    AbstractBaseIncomingCategoryListDataAccess,
    AbstractBaseRevenueCategoryListDataAccess,
)
from budget.domain.use_cases.base.base import AbstractBaseOutput
from budget.domain.use_cases.base.categories import (
    AbstractIncomingCategoryListUseCase,
    AbstractRevenueCategoryListUseCase,
)
from budget.domain.use_cases.features import (
    GetDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateDataAccessUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
)


class IncomingCategoryListUseCase(
    AbstractIncomingCategoryListUseCase,
    GetDataAccessUseCaseMixin[AbstractIncomingCategoryListUseCase],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):

    data_access: AbstractBaseIncomingCategoryListDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self):
        super().__init__()
        self.result = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        incoming_categories = self.data_access().get_incoming_categories()
        if not incoming_categories:
            return self._build_output()
        for category in incoming_categories:
            self.result.append(category.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output


class RevenueCategoryListUseCase(
    AbstractRevenueCategoryListUseCase,
    GetDataAccessUseCaseMixin[AbstractRevenueCategoryListUseCase],
    ValidateDataAccessUseCaseMixin,
    GetOutputResponseUseCaseMixin,
    ValidateOutputResponseUseCaseMixin,
):

    data_access: AbstractBaseRevenueCategoryListDataAccess = None
    output_response: AbstractBaseOutput = None

    def __init__(self):
        super().__init__()
        self.result = []

    def execute(self, *args, **kwargs):
        self.output_response.data = []
        revenue_categories = self.data_access().get_revenue_categories()
        if not revenue_categories:
            return self._build_output()
        for category in revenue_categories:
            self.result.append(category.to_dict())
        return self._build_output()

    def _build_output(self):
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output
