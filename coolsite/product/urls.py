from django.urls import path
from django.views.decorators.cache import cache_page

from product.views import (AboutUs, Baskets, ContactView, HomeView, Order,
                           ProductDetail, Success, Tags, basket_add,
                           basket_delete, basket_remove, comment_add)

urlpatterns = [
    path('', cache_page(3)(HomeView.as_view()), name='home'),
    path('product/<slug:product_slug>/', ProductDetail.as_view(), name='product'),
    path('tag/<slug:tag_slug>/', Tags.as_view(), name='tags'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('basket_delete/<int:basket_id>/', basket_delete, name='basket_delete'),
    path('basket/', Baskets.as_view(), name='baskets'),
    path('order/', Order.as_view(), name='order'),
    path('about_us/', AboutUs.as_view(), name='about_us'),
    path('comment/<int:product_id>/', comment_add, name='comment_add'),
    path('success/', Success.as_view(), name='success'),
    path('contact/', ContactView.as_view(), name='contact'),
]
