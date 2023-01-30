from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

# Create your models here.
class HomePageSlideShow(TimeStampedModel):
    slide_0_title = models.CharField(max_length=40, blank=False)
    slide_1_title = models.CharField(max_length=40, blank=False)
    slide_2_title = models.CharField(max_length=40, blank=False)

    slide_0_text = models.CharField(max_length=100, blank=False)
    slide_1_text = models.CharField(max_length=100, blank=False)
    slide_2_text = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'HomePageSlideShow'

    
class InstagramSection(TimeStampedModel):
    instagram_0_image = models.ImageField(upload_to='instagram/%Y/%m/%d')
    instagram_1_image = models.ImageField(upload_to='instagram/%Y/%m/%d')
    instagram_2_image = models.ImageField(upload_to='instagram/%Y/%m/%d')
    instagram_3_image = models.ImageField(upload_to='instagram/%Y/%m/%d')
    instagram_4_image = models.ImageField(upload_to='instagram/%Y/%m/%d')

    instagram_0_text = models.TextField()
    instagram_1_text = models.TextField()
    instagram_2_text = models.TextField()
    instagram_3_text = models.TextField()
    instagram_4_text = models.TextField()

    def __str__(self):
        return 'InstagramSection'


class AboutPage(TimeStampedModel):
    about = models.TextField()
    image = models.ImageField(upload_to='about/%Y/%m/%d')
    
    def __str__(self):
        return 'AboutPage'


class PoliticPage(TimeStampedModel):
    content = RichTextField()

    def __str__(self):
        return 'Politic'


class FaQs(TimeStampedModel):
    title = models.CharField(max_length=80, blank=False)
    text = RichTextField()
    faq_id = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return 'FaQs'
