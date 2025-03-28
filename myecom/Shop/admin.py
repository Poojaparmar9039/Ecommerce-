from django.contrib import admin
from .models import product,address,order_details,delivery_update
# Register your models here.    
admin.site.register(product)
admin.site.register(address)
admin.site.register(order_details)
admin.site.register(delivery_update)

