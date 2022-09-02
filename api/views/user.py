from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from api.serializers.user import UserSerializer

class UserView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer