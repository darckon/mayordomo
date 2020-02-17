from core.models import (
    User, Butler)
from core.serializers import (
    UserSerializer, ButlerSerializer)
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


class ButlerViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Butler.objects.all()
    serializer_class = ButlerSerializer
    filter_fields = '__all__'
    filter_backends = (DjangoFilterBackend,)