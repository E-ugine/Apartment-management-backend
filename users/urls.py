from django.urls import path, include
from .views import RegisterView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LandlordOnlyView, CaretakerOnlyView, TenantOnlyView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("test/landlord/", LandlordOnlyView.as_view(), name="test_landlord"),
    path("test/caretaker/", CaretakerOnlyView.as_view(), name="test_caretaker"),
    path("test/tenant/", TenantOnlyView.as_view(), name="test_tenant"),
    path('', include(router.urls)),
]
