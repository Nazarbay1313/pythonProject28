from django.contrib import admin

from product.models import Basket, Comment, Product, ProductShots, Tag

# Register your models here.

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(ProductShots)
admin.site.register(Basket)
