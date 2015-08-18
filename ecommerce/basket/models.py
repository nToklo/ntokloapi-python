from django.db import models
from productcatalog.models import Product
from django.contrib.auth.models import User

PURCHASE_CHOICES = (
    (0, 'Review'),
    (1, 'Checkout'),
    (2, 'Purchase'),
    (3, 'Confirmation')
)


class CartItem(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    products = models.ManyToManyField(Product)
    status = models.IntegerField(choices=PURCHASE_CHOICES, default=0)

    class Meta:
        ordering = ['pub_date']

    def total(self):
        final_price = 0
        for product in self.products.all():
            price = self.quantity * product.price_in_sterling
            final_price += price
        return str(final_price)

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price
