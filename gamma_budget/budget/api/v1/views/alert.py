from budget.api.v1.mixins import (
    ExecuteUseCaseOnCreateMixin,
    ExecuteUseCaseOnDestroyMixin,
    ExecuteUseCaseOnGetMixin,
    ExecuteUseCaseOnPutMixin,
)
from budget.api.v1.serializers.alert import (
    AlertSerializer,
    AlertTriggerSerializer,
    AlertUpdateSerializer,
)
from budget.api_output import DjangoApiOutput
from budget.domain.use_cases import (
    AlertCreateUseCase,
    AlertDeleteUseCase,
    AlertListUseCase,
    AlertSendEmailUseCase,
    AlertUpdateUseCase,
)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class AlertCreateAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    """
    API endpoint for creating alert budget records.

    Extends:
        APIView
        ExecuteUseCaseOnCreateMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = AlertSerializer
    serializer_create = AlertSerializer
    use_case_create = AlertCreateUseCase
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
            "user_email": request.data.get("user_email"),
            "revenue_id": request.data.get("revenue_id"),
            "message": request.data.get("message"),
            "alert_date": request.data.get("alert_date"),
        }
        return data


class AlertListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    """
    API endpoint for listing alert budget records.

    Extends:
        APIView
        ExecuteUseCaseOnGetMixin
    """

    permission_classes = (AllowAny,)
    serializer_class = AlertSerializer
    use_case_retrieve = AlertListUseCase
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


class AlertUpdateAPIView(APIView, ExecuteUseCaseOnPutMixin):
    """
    API endpoint for updating an existing alert budget record.

    Extends:
        APIView
        ExecuteUseCaseOnPutMixin
    """

    permission_classes = (AllowAny,)
    update_serializer_class = AlertUpdateSerializer
    serializer_class = AlertUpdateSerializer
    use_case = AlertUpdateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the alert record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        data = {
            "user_email": request.data.get("user_email"),
            "revenue_id": request.data.get("revenue_id"),
            "message": request.data.get("message"),
            "alert_date": request.data.get("alert_date"),
        }
        return {"user_id": user_id, "alert_id": id, "data": data}


class AlertDeleteAPIView(APIView, ExecuteUseCaseOnDestroyMixin):
    """
    API endpoint for deleting an existing alert budget record.

    Extends:
        APIView
        ExecuteUseCaseOnDestroyMixin
    """

    permission_classes = (AllowAny,)
    serializer = AlertSerializer
    use_case_destroy = AlertDeleteUseCase
    use_case_output: type[DjangoApiOutput] | None = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        """
        Get keyword arguments for the use case.

        Args:
        ----
            request: HTTP request object.
            user_id: ID of the user.
            id: ID of the alert record.

        Returns:
        -------
            dict: Keyword arguments.
        """
        return {"user_id": user_id, "alert_id": id}


class AlertsEmailTriggerAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    """
    API endpoint for triggering the sending of alert emails.

    Extends:
        APIView
        ExecuteUseCaseOnCreateMixin
    """

    permission_classes = (AllowAny,)
    use_case = AlertSendEmailUseCase
    use_case_output = DjangoApiOutput
    serializer_class = AlertTriggerSerializer
    serializer_create = AlertTriggerSerializer
