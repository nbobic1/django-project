from django.urls import re_path

from core.views.auth import RegistrationView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views.post import ContentView, PostsListView, PostView

app_name = "core"


urlpatterns = [
    re_path(r"^user/?$", UserView.as_view(), name="user"),
    re_path(r"^login/?$", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r"^token/refresh/?$", TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r"^register/?$", RegistrationView.as_view(), name="registration"),
    re_path(r"^posts/?$", PostsListView.as_view(), name='posts'),
    re_path(r"^post(/(?P<post_id>\d+))?/?$", PostView.as_view(), name='post'),
    re_path(r"^content(/(?P<content_id>\d+))?/?$", ContentView.as_view(), name='content'),
]
