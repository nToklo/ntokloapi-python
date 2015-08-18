from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from basket.models import CartItem
from productcatalog.models import Product
from django.conf import settings
from django.contrib.sites.models import Site
import ntokloapi


def basket(request):
    basket, created = CartItem.objects.get_or_create(status=0, user=request.user)
    site_url = Site.objects.get(id=1).domain
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "preview"
            }
        ],
        "listing": {
            "items": []
        },
        "user": {
            "visitor_id": request.user.id
        },
        "page": {
            "type": "review"
        }
    }
    if basket.products.all():
        for product in basket.products.all():
            details = {}
            details["id"] = str(product.id)
            details["name"] = product.name
            details["description"] = product.description
            details["image_url"] = "{}{}".format(site_url, product.photo.url)
            details["vendor"] = product.manufacturer.name
            details["unit_price"] = str(product.price_in_sterling)
            uv["listing"]["items"].append(details)
        print uv
        event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
        response = event.send(uv)
        print response
        print basket
        print basket.products.all()
    return render_to_response('basket.html', {'basket': basket},
                              RequestContext(request))


def cart_add(request, product_id):
    cart, created = CartItem.objects.get_or_create(status=0, user=request.user)
    print cart
    print cart.user
    print created
    product = Product.objects.get(id=product_id)
    print product
    cart.products.add(product)
    cart.save()
    return HttpResponse("Item added")


def purchase(request):
    basket = CartItem.objects.get(status=0, user=request.user)
    basket.status = 2
    basket.save()
    uv = {
        "version": "1.2",
        "events": [
            {
                "category": "conversion_funnel",
                "action": "purchase"
            }
        ],
        "transaction": {
            "line_items": []
        },
        "user": {
            "user.id": "request.user.id"
        },
        "page": {
            "type": "review"
        }
    }
    for product in basket.products.all():
        details = {}
        details["id"] = str(product.id)
        details["name"] = product.name
        details["description"] = product.description
        details["image_url"] = product.photo.url
        details["vendor"] = product.manufacturer.name
        details["unit_price"] = int(product.price_in_sterling)
        details["total"] = int(float(basket.total()))
        uv["transaction"]["line_items"].append(details)
    print uv
    event = ntokloapi.Event(settings.API_KEY, settings.API_SECRET)
    response = event.send(uv)
    print response
    return HttpResponse("Purchase complete")
