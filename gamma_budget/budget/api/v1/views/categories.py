from budget.api.v1.mixins import ExecuteUseCaseOnGetMixin
from budget.api.v1.serializers.categories import (
    IncomingCategoryListSerializer,
    RevenueCategoryListSerializer,
)
from budget.api_output import DjangoApiOutput
from budget.domain.use_cases.categories import (
    IncomingCategoryListUseCase,
    RevenueCategoryListUseCase,
)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class IncomingCategoryListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API view for retrieving a list of IncomingCategory instances.

    This view handles GET requests to retrieve a list of incoming categories. It uses
    the IncomingCategoryListUseCase to process the data and returns the result through
    a Django API output.

    """

    permission_classes = (AllowAny,)
    serializer_class = IncomingCategoryListSerializer
    use_case_retrieve = IncomingCategoryListUseCase
    use_case_output = DjangoApiOutput


class RevenueCategoryListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API view for retrieving a list of RevenueCategory instances.

    This view handles GET requests to retrieve a list of revenue categories. It uses
    the RevenueCategoryListUseCase to process the data and returns the result through
    a Django API output.

    """

    permission_classes = (AllowAny,)
    serializer_class = RevenueCategoryListSerializer
    use_case_retrieve = RevenueCategoryListUseCase
    use_case_output = DjangoApiOutput
