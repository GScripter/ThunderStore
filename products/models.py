from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


class Category(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250, blank=False)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default='no_image')
    price = models.FloatField(max_length=10, blank=False)
    description = RichTextField()
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


NOTA = (
    ('péssimo','péssimo'),
    ('ruim','ruim'),
    ('bom','bom'),
    ('excelente','excelente'),
    ('maravilhoso','maravilhoso'),
)

class Assessment(TimeStampedModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='procfile/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=100, blank=False)
    text = models.CharField(max_length=350, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    choice_nota = models.CharField(choices=NOTA, max_length=12, default='ruim')

    def __str__(self):
        return f'{self.product}'
