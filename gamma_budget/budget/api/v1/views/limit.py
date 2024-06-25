from budget.api.v1.mixins import (
    ExecuteUseCaseOnCreateMixin,
    ExecuteUseCaseOnDestroyMixin,
    ExecuteUseCaseOnGetMixin,
    ExecuteUseCaseOnPutMixin,
)
from budget.api.v1.serializers.limit import LimitSerializer, LimitUpdateSerializer
from budget.api_output import DjangoApiOutput
from budget.domain.use_cases import (
    LimitCreateUseCase,
    LimitDeleteUseCase,
    LimitListUseCase,
    LimitUpdateUseCase,
)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LimitCreateAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    """
    API endpoint for creating limit budget records.

    Extends:
        APIView
        ExecuteUseCaseOnCreateMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = LimitSerializer
    serializer_create = LimitSerializer
    use_case_create = LimitCreateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.

        Returns:
        -------
            dict: Keyword arguments.
        """
        data = {
            "user_id": user_id,
            "limit": request.data.get("limit"),
            "limit_date": request.data.get("limit_date"),
            "amount": request.data.get("amount"),
            "category": request.data.get("category"),
        }
        return data


class LimitListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for listing limit budget records.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = LimitSerializer
    use_case_retrieve = LimitListUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id}


class LimitUpdateAPIView(APIView, ExecuteUseCaseOnPutMixin):
    """
    API endpoint for updating an existing limit budget record.

    Extends:
        APIView
        ExecuteUseCaseOnPutMixin
    """

    permission_classes = (AllowAny,)
    update_serializer_class = LimitUpdateSerializer
    serializer_class = LimitUpdateSerializer
    use_case = LimitUpdateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the limit record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        data = {
            "limit": request.data.get("limit"),
            "amount": request.data.get("amount"),
        }
        return {"user_id": user_id, "limit_id": id, "data": data}


class LimitDeleteAPIView(APIView, ExecuteUseCaseOnDestroyMixin):
    """
    API endpoint for deleting an existing limit budget record.

    Extends:
        APIView
        ExecuteUseCaseOnDestroyMixin
    """

    permission_classes = (AllowAny,)
    serializer = LimitSerializer
    use_case_destroy = LimitDeleteUseCase
    use_case_output: type[DjangoApiOutput] | None = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the limit record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "limit_id": id}
