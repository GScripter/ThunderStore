from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . models import Product, Category, ProductImage
from page.models import HomePageSlideShow, InstagramSection
from django.db.models import Q
from orders.models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.models import User

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
        return Product.objects.filter(category__name=self.kwargs['str'], is_available=True).order_by('-modified')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['str']
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


@method_decorator(login_required, name='dispatch')
class TrackerPageView(ListView):
    context_object_name = 'tracker_number'
    paginate_by = 1
    template_name = 'tracker.html'

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)


    def get_context_data(self, **kwargs):
        order = False
        if Order.objects.filter(user_id=self.request.user.id):
            order = True
        context = super().get_context_data(**kwargs)
        context['order'] = order
        return context
