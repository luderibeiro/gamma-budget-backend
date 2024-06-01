from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

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


class IncomingCreateAPIView(APIView, ExecuteUseCaseOnCreateMixin):
    permission_classes = (AllowAny,)
    serializer_class = IncomingCreateSerializer
    serializer_create = IncomingCreateSerializer
    use_case_create = IncomingCreateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, *args, **kwargs):
        data = {}
        data = {
            "user_id": user_id,
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "category": request.data.get("category"),
        }
        return data


class IncomingListAPIView(APIView, ExecuteUseCaseOnGetMixin):
    permission_classes = (AllowAny,)
    serializer_class = IncomingListSerializer
    use_case_retrieve = IncomingListUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id):
        return {"user_id": user_id}


class IncomingDetailAPIView(APIView, ExecuteUseCaseOnGetMixin):
    permission_classes = (AllowAny,)
    serializer_class = IncomingDetailSerializer
    use_case_retrieve = IncomingRetrieveUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, id, user_id):
        return {"user_id": user_id, "incoming_id": id}


class IncomingUpdateAPIView(APIView, ExecuteUseCaseOnPutMixin):
    permission_classes = (AllowAny,)
    update_serializer_class = IncomingUpdateSerializer
    serializer_class = IncomingUpdateSerializer
    use_case = IncomingUpdateUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        data = {}
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "amount": request.data.get("amount"),
            "category": request.data.get("category"),
        }
        return {"user_id": user_id, "incoming_id": id, "data": data}


class IncomingDeleteAPIView(APIView, ExecuteUseCaseOnDestroyMixin):
    permission_classes = (AllowAny,)
    serializer = IncomingDeleteSerializer
    use_case_destroy = IncomingDeleteUseCase
    use_case_output = DjangoApiOutput

    def get_use_case_kwargs(self, request, user_id, id, *args, **kwargs):
        return {"user_id": user_id, "incoming_id": id}
