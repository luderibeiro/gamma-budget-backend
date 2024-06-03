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
    """
    Use case for handling a list of IncomingCategory instances.

    This use case retrieves incoming categories through a data access layer, processes
    them, and prepares an output response.

    Attributes:
    ----------
    data_access : type[AbstractIncomingCategoryListUseCase] | None
        The data access layer used to retrieve incoming categories.
    output_response : type[AbstractBaseOutput] | None
        The output response object that will be populated with the result.
    result : list
        A list to store the processed incoming categories.
    """

    data_access: type[AbstractIncomingCategoryListUseCase] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self):
        """
        Initializes the IncomingCategoryListUseCase.

        This constructor initializes the result list and calls the parent constructor.
        """
        super().__init__()
        self.result = []

    def execute(self, *args, **kwargs):
        """
        Executes the use case to retrieve and process incoming categories.

        This method retrieves incoming categories through the data access layer, processes
        them into a list of dictionaries, and builds the output response.

        Returns:
        -------
        AbstractBaseOutput
            The output response populated with the processed incoming categories.
        """
        self.output_response.data = []
        incoming_categories = self.data_access().get_incoming_categories()
        if not incoming_categories:
            return self._build_output()
        for category in incoming_categories:
            self.result.append(category.to_dict())
        return self._build_output()

    def _build_output(self):
        """
        Builds the output response.

        This method populates the output response with the result list.

        Returns:
        -------
        AbstractBaseOutput
            The output response populated with the processed incoming categories.
        """
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
    """
    Use case for handling a list of RevenueCategory instances.

    This use case retrieves revenue categories through a data access layer, processes
    them, and prepares an output response.

    Attributes:
    ----------
    data_access : type[AbstractRevenueCategoryListUseCase] | None
        The data access layer used to retrieve revenue categories.
    output_response : type[AbstractBaseOutput] | None
        The output response object that will be populated with the result.
    result : list
        A list to store the processed revenue categories.
    """

    data_access: type[AbstractRevenueCategoryListUseCase] | None = None
    output_response: type[AbstractBaseOutput] | None = None

    def __init__(self):
        """
        Initializes the RevenueCategoryListUseCase.

        This constructor initializes the result list and calls the parent constructor.
        """
        super().__init__()
        self.result = []

    def execute(self, *args, **kwargs):
        """
        Executes the use case to retrieve and process revenue categories.

        This method retrieves revenue categories through the data access layer, processes
        them into a list of dictionaries, and builds the output response.

        Returns:
        -------
        AbstractBaseOutput
            The output response populated with the processed revenue categories.
        """
        self.output_response.data = []
        revenue_categories = self.data_access().get_revenue_categories()
        if not revenue_categories:
            return self._build_output()
        for category in revenue_categories:
            self.result.append(category.to_dict())
        return self._build_output()

    def _build_output(self):
        """
        Builds the output response.

        This method populates the output response with the result list.

        Returns:
        -------
        AbstractBaseOutput
            The output response populated with the processed revenue categories.
        """
        self.output = self.get_output_response()
        self.output.data = self.result
        return self.output
