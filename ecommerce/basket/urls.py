from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^purchase/$', views.purchase, name='purchase'),
    url(r'^cart_add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^$', views.basket, name='basket'),
]
