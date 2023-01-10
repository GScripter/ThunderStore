from django.urls import path
from . views import HomePageView, ProductsPageView, ProductDetailPageView, ProductsCategoryView,  SearchResults, TrackerPageView

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('produtos/', ProductsPageView.as_view(), name='products'),
    path('produtos/<slug:slug>/', ProductDetailPageView.as_view(), name='product_detail'),
    path('produtos/categoria/<str:str>/', ProductsCategoryView.as_view(), name='filter_products'),
    path('resultados/', SearchResults.as_view(), name='search_results'),
    path('produto/rastreio/', TrackerPageView.as_view(), name='tracker'),
]

