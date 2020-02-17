from django.urls import include, path
from rest_framework import routers
from core import api as core_api

router = routers.DefaultRouter()

router.register('api/v1/users', core_api.UserViewSet),
router.register('api/v1/butlers', core_api.ButlerViewSet),


urlpatterns = [

    # API
    path('', include(router.urls))

]