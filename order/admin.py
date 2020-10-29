from django.contrib import admin
from order.models import Coffee,Desserts,Goods,Carts

# Register your models here.

#김은수
admin.site.register(Coffee)
admin.site.register(Desserts)
admin.site.register(Goods)
admin.site.register(Carts)