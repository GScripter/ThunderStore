from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Product, Category, ProductImage
from page.models import HomePageSlideShow, InstagramSection
from django.db.models import Q
from orders.models import Order, Item
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.models import User
from . models import Assessment
from django.urls import reverse, reverse_lazy

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
    template_name = 'detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        context['product_image'] = ProductImage.objects.filter(product__slug=self.kwargs['slug'])
        product = Product.objects.get(slug=self.kwargs['slug'])
        context['assessments'] = Assessment.objects.filter(product=product).order_by('-modified')[:1]
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


class AssessmentPageView(TemplateView):
    template_name = 'assessment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.kwargs['id']
        product = Product.objects.get(id=self.kwargs['id'])
        context['assessments'] = Assessment.objects.filter(product=product).order_by('-modified')
        return context

    def post(self, request, **kwargs):
        product = Product.objects.get(id=self.kwargs['id'])
        Assessment.objects.create(user_id=self.request.user.id, image=self.request.user.procfile_photo, name=self.request.user.name, text=self.request.POST['assessment'], product=product)
        return redirect('products:product_detail', product.slug)


@method_decorator(login_required, name='dispatch')
class DeleteAssessment(DeleteView):
    template_name = 'delete_assessment.html'

    def get_queryset(self):
        return Assessment.objects.filter(user_id=self.request.user.id)

    def get_success_url(self, **kwargs):
        product = Product.objects.get(id=self.kwargs['id'])
        return reverse('products:product_detail', kwargs={'slug': product.slug})


@method_decorator(login_required, name='dispatch')
class UpdateAssessment(UpdateView):
    template_name = 'update_assessment.html'
    fields = ['text']

    def get_queryset(self):
        return Assessment.objects.filter(user_id=self.request.user.id)

    def get_success_url(self, **kwargs):
        product = Product.objects.get(id=self.kwargs['id'])
        return reverse('products:product_detail', kwargs={'slug': product.slug})

