from django.contrib import admin
from .models import Item, Topping, Sub, Item_price_by_size, Item_price_no_size, Orders

# Register your models here.

admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Item_price_by_size)
admin.site.register(Item_price_no_size)
admin.site.register(Orders)