from django.contrib import admin
from django.urls import include, path
from core import api as core_api
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# API Routers
from core.urls import router as core_router

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    #RestFramework
    path('api-auth/', include('rest_framework.urls')),

    # API
    path('core/', include(core_router.urls)),

    #RestFramework - JWT
    path('login/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
