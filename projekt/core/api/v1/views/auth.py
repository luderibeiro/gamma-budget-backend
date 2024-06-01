from core.api.v1.serializers.auth import AuthSerializer
from core.api.v1.serializers.user import UserSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


class AuthView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = AuthSerializer(data=request.data)
            if serializer.is_valid():
                user = None

                email = request.data.get("email", None)
                if email != None and len(email) > 0:
                    try:
                        user = User.objects.get(email=request.data["email"])
                        user = authenticate(username=user.email, password=request.data["password"])
                    except User.DoesNotExist:
                        pass

                if user is not None:
                    serializer = UserSerializer(user)
                    return Response(serializer.data, status.HTTP_200_OK)

                return Response("User not found!", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response("Server error! {}".format(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
