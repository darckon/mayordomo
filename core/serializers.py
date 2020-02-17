# -*- encoding: utf-8 -*-
from core.models import (
    User)
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework_jwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'