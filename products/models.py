from django.db import models

# Create your models here.



class ProductCategory(models.Model):
    name = models.CharField(max_length=68, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = "Категорія товару"
        verbose_name_plural = "Категорії товарів"


class Product(models.Model):
    name = models.CharField(max_length=68, blank=True, null=True, default=None)
    descpiption = models.TextField(blank=True, null=True, default=None)
    short_descpiption = models.TextField(blank=True, null=True, default=None)
    discount = models.IntegerField(blank=True, null=True, default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    prise = models.IntegerField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    Product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='img/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id


    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
