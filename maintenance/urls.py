from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MaintenanceRequestViewSet

router = DefaultRouter()
router.register(r'requests', MaintenanceRequestViewSet, basename='maintenance-request')

urlpatterns = [
    path('', include(router.urls)),
]


