from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(TimeStampedModel):
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=150, blank=False)
    subtitle = models.CharField(max_length=250, blank=False)
    slug = AutoSlugField(unique=True, populate_from='title', always_update=False)
    content = RichTextUploadingField()

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

