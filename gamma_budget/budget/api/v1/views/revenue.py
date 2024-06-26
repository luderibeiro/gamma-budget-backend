from budget.api.v1.mixins import (
    ExecuteUseCaseOnCreateMixin,
    ExecuteUseCaseOnDestroyMixin,
    ExecuteUseCaseOnGetMixin,
    ExecuteUseCaseOnPutMixin,
)
from budget.api.v1.serializers.revenue import (
    RevenueCreateSerializer,
    RevenueDeleteSerializer,
    RevenueDetailSerializer,
    RevenueListSerializer,
    RevenueUpdateSerializer,
)
from budget.api_output import DjangoApiOutput
from budget.domain.use_cases import (
    RevenueCreateUseCase,
    RevenueDeleteUseCase,
    RevenueListUseCase,
    RevenueRetrieveUseCase,
    RevenueUpdateUseCase,
)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RevenueCreateAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    """
    API endpoint for creating revenue records.

    Extends:
        APIView
        ExecuteUseCaseOnCreateMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = RevenueCreateSerializer
    serializer_create = RevenueCreateSerializer
    use_case_create = RevenueCreateUseCase
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
        paid = request.data.get("paid") == "true"

        data = {
            "user_id": user_id,
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "expiration_date": request.data.get("expiration_date"),
            "paid": paid,
            "payment_date": request.data.get("payment_date") if paid else None,
            "category": request.data.get("category"),
        }
        return data


class RevenueListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for listing revenue records.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = RevenueListSerializer
    use_case_retrieve = RevenueListUseCase
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


class RevenueDetailAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for retrieving a specific revenue record.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = RevenueDetailSerializer
    use_case_retrieve = RevenueRetrieveUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, id, user_id):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            id: ID of the revenue record.
            user_id: ID of the user.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "revenue_id": id}


class RevenueUpdateAPIView(APIView, ExecuteUseCaseOnPutMixin):
    """
    API endpoint for updating an existing revenue record.

    Extends:
        APIView
        ExecuteUseCaseOnPutMixin
    """

    # TODO: Falta atualizar o paid e payment_date
    permission_classes = (AllowAny,)
    update_serializer_class = RevenueUpdateSerializer
    serializer_class = RevenueUpdateSerializer
    use_case = RevenueUpdateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the revenue record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        data = {}
        paid = request.data.get("paid") == "true"
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "expiration_date": request.data.get("expiration_date"),
            "paid": paid,
            "payment_date": request.data.get("payment_date") if paid else None,
            "category": request.data.get("category"),
        }
        return {"user_id": user_id, "revenue_id": id, "data": data}


class RevenueDeleteAPIView(APIView, ExecuteUseCaseOnDestroyMixin):
    """
    API endpoint for deleting an existing revenue record.

    Extends:
        APIView
        ExecuteUseCaseOnDestroyMixin
    """

    permission_classes = (AllowAny,)
    serializer = RevenueDeleteSerializer
    use_case_destroy = RevenueDeleteUseCase
    use_case_output: type[DjangoApiOutput] = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the revenue record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "revenue_id": id}
