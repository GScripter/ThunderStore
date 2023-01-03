from django.urls import path
from . views import BlogHomePageView, BlogPostView

app_name = 'blog'

urlpatterns = [
    path('', BlogHomePageView.as_view(), name='home-page-view'),
    path('post/<slug:slug>/', BlogPostView.as_view(), name='blog-post-view'),
]


