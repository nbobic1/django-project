from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import User
from core.serializers import UserSerializer
from core.utils.pagination import HundredSetPagination


class UsersListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    pagination_class = HundredSetPagination
    queryset = User.objects.all()
