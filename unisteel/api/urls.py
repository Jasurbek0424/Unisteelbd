from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ContactsViewSet, RekvizitiViewSet, CompaniyInfoViewSet, ServisesViewSet

product_router = DefaultRouter()
product_router.register(r'Products', ProductViewSet)
product_router.register(r'contacts', ContactsViewSet)
product_router.register(r'rekviziti', RekvizitiViewSet)
product_router.register(r'information', CompaniyInfoViewSet)
product_router.register(r'servises', ServisesViewSet)