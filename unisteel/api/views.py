from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import Product, Contacts, Rekviziti, CompaniyInfo, Servises
from .serializers import ProductSerializer, ContactsSerializer, RekvizitiSerializer, CompaniyInfoSerializer, ServisesSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RekvizitiViewSet(ModelViewSet):
    queryset = Rekviziti.objects.all()
    serializer_class = RekvizitiSerializer

class CompaniyInfoViewSet(ModelViewSet):
    queryset = CompaniyInfo.objects.all()
    serializer_class = CompaniyInfoSerializer


class ServisesViewSet(ModelViewSet):
    queryset = Servises.objects.all()
    serializer_class = ServisesSerializer