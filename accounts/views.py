from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from accounts.serializers import CreateUserSerializer


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer
