from django.contrib import admin
from . models import HomePageSlideShow, InstagramSection, AboutPage, PoliticPage, FaQs

# Register your models here.
admin.site.register(HomePageSlideShow)
admin.site.register(AboutPage)
admin.site.register(PoliticPage)
admin.site.register(InstagramSection)
admin.site.register(FaQs)
