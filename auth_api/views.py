from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from auth_api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['retrieve', 'update', 'destroy', 'list']:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
