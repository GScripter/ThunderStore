from django.urls import path
from . views import AboutPageView, ContactPageView, ConfigPageView, AccountDelete, CancelPageView, PoliticPageView, SuccessPageView

app_name = 'page'

urlpatterns = [
    path('sobre/', AboutPageView.as_view(), name='about'),
    path('politica/', PoliticPageView.as_view(), name='politic'),
    path('contato/', ContactPageView.as_view(), name='contact'),
    path('configuracao/<int:pk>/', ConfigPageView.as_view(), name='config'),
    path('deletar_conta/<int:pk>/', AccountDelete.as_view(), name='account_delete'),
    path('pedido/cancelado/', CancelPageView.as_view(), name='cancel'),
    path('pedido/sucesso/', SuccessPageView.as_view(), name='success'),
]


