from django.urls import path
from rest_framework.routers import DefaultRouter

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from libros.api.view import LibrosApiViewSet

router_libros = DefaultRouter()

router_libros.register(prefix="libros", basename="libros", viewset=LibrosApiViewSet)