from rest_framework.serializers import ModelSerializer
from ..models import Product, Contacts, Rekviziti, CompaniyInfo, Servises

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'gost', 'category', 'country', 'size', 'content', 'get_photo', 'photo')

class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'full_name', 'contact', 'comment', 'add_time')
    
class RekvizitiSerializer(ModelSerializer):
    class Meta:
        model = Rekviziti
        fields = '__all__'

class CompaniyInfoSerializer(ModelSerializer):
    class Meta:
        model = CompaniyInfo
        fields = '__all__'

class ServisesSerializer(ModelSerializer):
    class Meta:
        model = Servises
        fields = '__all__'