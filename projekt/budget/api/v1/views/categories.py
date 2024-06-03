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
from rest_framework import exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class IncomingCategoryListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    permission_classes = (AllowAny,)
    serializer_class = IncomingCategoryListSerializer
    use_case_retrieve = IncomingCategoryListUseCase
    use_case_output = DjangoApiOutput


class RevenueCategoryListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    permission_classes = (AllowAny,)
    serializer_class = RevenueCategoryListSerializer
    use_case_retrieve = RevenueCategoryListUseCase
    use_case_output = DjangoApiOutput
