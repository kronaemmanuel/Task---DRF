from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from auth_api.views import UserList

urlpatterns = format_suffix_patterns([
    path('users/', UserList.as_view(), name='users-list')
])
