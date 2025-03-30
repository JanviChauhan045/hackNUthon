from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'farmers', views.FarmerProfileViewSet)
# Register all other viewsets

urlpatterns = [
    path('api/', include(router.urls)),
]