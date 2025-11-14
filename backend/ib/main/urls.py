from django.urls import path, include, re_path
from .models import Organization
from rest_framework import routers

from .views import OrganizationViewSet

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
urlpatterns += router.urls