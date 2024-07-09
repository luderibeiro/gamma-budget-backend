from budget.api.v1.mixins import (
    ExecuteUseCaseOnCreateMixin,
    ExecuteUseCaseOnDestroyMixin,
    ExecuteUseCaseOnGetMixin,
    ExecuteUseCaseOnPutMixin,
)
from budget.api.v1.serializers.incoming import (
    IncomingCreateSerializer,
    IncomingDeleteSerializer,
    IncomingDetailSerializer,
    IncomingListSerializer,
    IncomingUpdateSerializer,
)
from budget.api_output import DjangoApiOutput
from budget.domain.use_cases import (
    IncomingCreateUseCase,
    IncomingDeleteUseCase,
    IncomingListUseCase,
    IncomingRetrieveUseCase,
    IncomingUpdateUseCase,
)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class IncomingCreateAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    """
    API endpoint for creating incoming budget records.

    Extends:
        APIView
        ExecuteUseCaseOnCreateMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = IncomingCreateSerializer
    serializer_create = IncomingCreateSerializer
    use_case_create = IncomingCreateUseCase
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
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "incoming_date": request.data.get("incoming_date"),
            "category": request.data.get("category"),
        }
        return data


class IncomingListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for listing incoming budget records.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = IncomingListSerializer
    use_case_retrieve = IncomingListUseCase
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


class IncomingDetailAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for retrieving a specific incoming budget record.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = IncomingDetailSerializer
    use_case_retrieve = IncomingRetrieveUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, id, user_id):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            id: ID of the incoming record.
            user_id: ID of the user.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "incoming_id": id}


class IncomingUpdateAPIView(APIView, ExecuteUseCaseOnPutMixin):
    """
    API endpoint for updating an existing incoming budget record.

    Extends:
        APIView
        ExecuteUseCaseOnPutMixin
    """

    permission_classes = (AllowAny,)
    update_serializer_class = IncomingUpdateSerializer
    serializer_class = IncomingUpdateSerializer
    use_case = IncomingUpdateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the incoming record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "incoming_date": request.data.get("incoming_date"),
            "category": request.data.get("category"),
        }
        return {"user_id": user_id, "incoming_id": id, "data": data}


class IncomingDeleteAPIView(APIView, ExecuteUseCaseOnDestroyMixin):
    """
    API endpoint for deleting an existing incoming budget record.

    Extends:
        APIView
        ExecuteUseCaseOnDestroyMixin
    """

    permission_classes = (AllowAny,)
    serializer = IncomingDeleteSerializer
    use_case_destroy = IncomingDeleteUseCase
    use_case_output: type[DjangoApiOutput] | None = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the incoming record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "incoming_id": id}
