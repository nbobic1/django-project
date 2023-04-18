from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.serializers import RegistrationSerializer, UserSerializer


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

