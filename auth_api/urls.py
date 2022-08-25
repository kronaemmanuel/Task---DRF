from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from auth_api.views import UserList, UserRegister, api_root

urlpatterns = format_suffix_patterns([
    path('users/', api_root, name='users'),
    path('users/list/', UserList.as_view(), name='users-list'),
    path('users/register/', UserRegister.as_view(), name='users-register')
])
