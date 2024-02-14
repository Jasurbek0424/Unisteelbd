from rest_framework.serializers import ModelSerializer,SerializerMethodField
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
    image=SerializerMethodField()
    class Meta:
        model = Servises
        fields = '__all__'
    
    def get_image(self,obj):
        try:
            return f"https://2543655-yo82697.twc1.net{obj.image.url}"
        except:
            return "https://m.media-amazon.com/images/I/21cOE-lrhBL._AC_UF1000,1000_QL80_.jpg"
        
