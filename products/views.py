from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . models import Product, Category, ProductImage
from page.models import HomePageSlideShow, InstagramSection
from django.db.models import Q

# Create your views here.
class HomePageView(ListView):
    queryset = Product.objects.filter(featured=True)
    context_object_name = 'featured'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if HomePageSlideShow.objects.all():
            context['HomePageSlideShow'] = HomePageSlideShow.objects.all().order_by('-modified')[0]
        if InstagramSection.objects.all():
            context['InstagramSection'] = InstagramSection.objects.all().order_by('-modified')[0]
        return context



class ProductsPageView(ListView):
    paginate_by = 9
    queryset = Product.objects.filter(is_available=True).order_by('-modified')
    context_object_name = 'products'
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-modified')
        return context



class ProductDetailPageView(ListView):
    queryset = Product.objects.filter(is_available=True).order_by('modified')
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        context['product_image'] = ProductImage.objects.filter(product__slug=self.kwargs['slug'])
        return context



class ProductsCategoryView(ListView):
    paginate_by = 9
    context_object_name = 'products'
    template_name = 'category.html'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'], is_available=True).order_by('-modified')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['slug']
        return context



class SearchResults(ListView):
    paginate_by = 9
    template_name = 'search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return products


