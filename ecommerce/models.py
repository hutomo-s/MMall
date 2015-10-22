from django.contrib.auth.models import User
from django.db import models

from django_enumfield import enum

# Create your models here.
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, upload_to = 'pictures/%Y/%m/%d')
    slug = models.SlugField(blank=True)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + ' ' + self.brand.name

class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)

    def __str__(self):
        return self.name

class CartStatus(enum.Enum):
    CREATED = 1
    PAID = 2
    SHIPPED = 3
    DELIVERED = 4
    DONE = 5

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total = models.IntegerField()
    payment_date = models.DateTimeField(blank=True)
    status = enum.EnumField(CartStatus, default=CartStatus.CREATED)

    # def __str__(self):
    #     return self.id + ' ' + self.brand.name

class CartItem(models.Model):
    cart_id = models.ForeignKey('Cart')
    quantity = models.IntegerField()
    product_id = models.ForeignKey('Product')
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)