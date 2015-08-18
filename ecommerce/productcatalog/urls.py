from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
    url(r'^manufacturers/(?P<id>\d+)/$', views.manufacturers, name='manufacturers'),
    url(r'^category/(?P<id>\d+)/$', views.categories, name='categories'),
    url(r'^product/(?P<id>\d+)/$', views.products, name='product'),
    url(r'^manufacturer/$', views.manufacturer, name='manufacturer'),
    url(r'^category/$', views.category, name='category'),
    url(r'^products/$', views.product, name='products'),
    url(r'^$', views.index, name='index'),
]
