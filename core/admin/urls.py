from django.urls import re_path

from core.admin.views.post import AdminPostView, AdminPostCreateListView, AdminContentView

app_name = "core"

urlpatterns = [
    re_path(r"^post/?$", AdminPostCreateListView.as_view(), name='posts'),
    re_path(r"^post/(?P<id>\d+)/?$", AdminPostView.as_view(), name='post'),
    re_path(r"^content/(?P<id>\d+)/?$", AdminContentView.as_view(), name='post'),
]