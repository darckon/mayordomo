from core.models import (
    User)
from core.serializers import (
    UserSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from url_filter.integrations.drf import DjangoFilterBackend as UrlDjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = '__all__'
    filter_backends = (DjangoFilterBackend,)