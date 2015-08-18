from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='itemphotos')
    price_in_sterling = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField()
    instock = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name
