from django.contrib import admin

from .models import Product, Contacts, Rekviziti, Servises, CompaniyInfo

# Register your models here.


admin.site.register(Product)
admin.site.register(Contacts)
admin.site.register(Rekviziti)
admin.site.register(Servises)
admin.site.register(CompaniyInfo)