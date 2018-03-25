from django.contrib import admin

# Register your models here.
from .models import Book,Shopping_Cart,Selling_Cart,Order,Paid_Order,Comment

admin.site.register(Book)
admin.site.register(Shopping_Cart)
admin.site.register(Selling_Cart)
admin.site.register(Order)
admin.site.register(Paid_Order)
admin.site.register(Comment)
