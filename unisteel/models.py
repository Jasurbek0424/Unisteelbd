from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    gost = models.CharField(blank=True, null=True, max_length=255)
    category = models.CharField(max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    size = models.CharField(blank=True, null=True, max_length=500)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='photos/')
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return f"https://toounisteel.kz{self.photo.url}"
        except:
            return "https://m.media-amazon.com/images/I/21cOE-lrhBL._AC_UF1000,1000_QL80_.jpg"
        
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        

class Contacts(models.Model):
    full_name = models.CharField(max_length=300, default="Customer")
    contact = models.CharField(max_length=50)
    comment = models.TextField(default="No Comment")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    

class Rekviziti(models.Model):
    file = models.FileField(upload_to='rekvizit')

    def __str__(self):
        return self.file.name
    class Meta:
        verbose_name = 'Реквизит'
        verbose_name_plural = 'Реквизиты'

class CompaniyInfo(models.Model):
    address = models.CharField(max_length=255)
    number1 = models.CharField(blank=True, null=True, max_length=50)
    number2 = models.CharField(blank=True, null=True, max_length=50)
    number3 = models.CharField(blank=True, null=True, max_length=50)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

class Servises(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='serviseImages/')
    infoPreTitle = models.TextField(blank=True, null=True)
    infoTitle = models.CharField(blank=True, null=True, max_length=255)
    infoText = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
