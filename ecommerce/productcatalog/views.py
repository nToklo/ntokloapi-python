import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from productcatalog.models import Product, Category, Manufacturer
from basket.models import CartItem

import ntokloapi


def index(request):
    product = Product.objects.all()[:5]
    category = Category.objects.all()
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    return render_to_response('index.html', {'category': category,
                              "product": product, 'basket': basket},
                              RequestContext(request))


def product(request):
    page_products = Product.objects.all()
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    print basket
    print basket.products.all()
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "browse"
            }
        ],
        "listing": {
            "items": []
        },
        "user": {
            "user_id": str(request.user.id)
        },
        "page": {
            "type": "products"
        }
    }
    for product in page_products:
        details = {}
        details["id"] = str(product.id)
        details["name"] = product.name
        details["description"] = product.description
        details["image_url"] = product.photo.url
        details["vendor"] = product.manufacturer.name
        details["unit_price"] = int(product.price_in_sterling)
        uv["listing"]["items"].append(details)
    print uv
    event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
    response = event.send(uv)
    print response
    return render_to_response('Products.html',
                              {'page_products': page_products,
                               'basket': basket},
                              RequestContext(request))


def products(request, id):
    product = Product.objects.get(id=id)
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    recommendation = ntokloapi.Recommendation(settings.API_KEY, settings.API_SECRET)
    productid = "{}".format(product.id)
    userid = "{}".format(request.user.id)
    recommendations = recommendation.get(productid=productid, userid=userid)
    print recommendations
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "preview"
            }
        ],
        "product": {
            "id": str(product.id),
            "name": product.name,
            "description": product.description,
            "image_url": product.photo.url,
            "vendor": product.manufacturer.name,
            "unit_price": int(product.price_in_sterling)
        },
        "user": {
            "user_id": str(request.user.id)
        },
        "page": {
            "type": "product",
            "breadcrumb": [product.category.name]

        }
    }
    if request.GET.get("tracker_id", ""):
        trackerid = {
            "category": "clickthrough_goals",
            "action": "recommendation-click",
            "tracker_id": recommendations["tracker_id"]
        }
        uv["events"].append(trackerid)
        print uv
    print recommendations
    event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
    response = event.send(uv)
    print uv
    print response
    return render_to_response('product.html', {"product": product,
                              'basket': basket, 'recommendations': recommendations},
                              RequestContext(request))


def category(request):
    page_category = Category.objects.all()
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    return render_to_response('category.html',
                              {'page_category': page_category,
                               'basket': basket},
                              RequestContext(request))


def categories(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "browse"
            }
        ],
        "listing": {
            "items": []
        },
        "user": {
            "visitor_id": request.user.id
        },
        "page": {
            "type": "category"
        }
    }
    for product in products:
        details = {}
        details["id"] = str(product.id)
        details["name"] = product.name
        details["description"] = product.description
        details["image_url"] = product.photo.url
        details["vendor"] = product.manufacturer.name
        details["unit_price"] = int(product.price_in_sterling)
        uv["listing"]["items"].append(details)
    print uv
    event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
    response = event.send(uv)
    print response
    return render_to_response('categories.html',
                              {"category": category, "products": products,
                               'basket': basket},
                              RequestContext(request))


def manufacturer(request):
    manufacturer = Manufacturer.objects.all()
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    return render_to_response("manufacturers.html",
                              {"manufacturer": manufacturer, 'basket': basket},
                              RequestContext(request))


def manufacturers(request, id):
    manufacturers = Manufacturer.objects.get(id=id)
    products = Product.objects.filter(manufacturer_id=manufacturers)
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "browse"
            }
        ],
        "listing": {
            "items": []
        },
        "user": {
            "visitor_id": request.user.id
        },
        "page": {
            "type": "manufacturers"
        }
    }
    for product in products:
        details = {}
        details["id"] = str(product.id)
        details["name"] = product.name
        details["description"] = product.description
        details["image_url"] = product.photo.url
        details["vendor"] = product.manufacturer.name
        details["unit_price"] = int(product.price_in_sterling)
        uv["listing"]["items"].append(details)
    print uv
    event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
    response = event.send(uv)
    print response
    return render_to_response('manufacture.html',
                              {"manufacturers": manufacturers,
                               "products": products, 'basket': basket},
                              RequestContext(request))
