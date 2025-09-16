"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import AdminOnlySpectacularAPIView, AdminOnlySwaggerView, AdminOnlyRedocView

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),  # DRF browsable API login/logout
    path('api/apartments/', include('apartments.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/notices/', include('notices.urls')),
    path('api/maintenance/', include('maintenance.urls')),
    # OpenAPI schema and UIs (admin only)
    path('api/schema/', AdminOnlySpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', AdminOnlySwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', AdminOnlyRedocView.as_view(url_name='schema'), name='redoc'),
]
