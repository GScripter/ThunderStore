from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class Category(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)

    def __str__(self):
        return self.name


# Create your models here.
class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250, blank=False)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default='no_image')
    price = models.FloatField(max_length=10, blank=False)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)
    description = models.TextField(blank=True)

