from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UnitViewSet

router = DefaultRouter()
router.register(r'units', UnitViewSet, basename='unit')

urlpatterns = [
    path('', include(router.urls)),
]


