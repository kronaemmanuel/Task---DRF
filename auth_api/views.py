from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from auth_api.serializers import UserRegisterSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users/list': reverse('users-list', request=request, format=format),
        'users/register': reverse('users-register', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
