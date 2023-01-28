from django.shortcuts import render 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from . models import AboutPage, PoliticPage, FaQs
from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class AboutPageView(ListView):
    queryset = AboutPage.objects.all().order_by('-modified')[0:1]
    context_object_name = 'about'
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def post(self, request):
        organize = (f"nome: {request.POST['name']}\ne-mail: {request.POST['email']}\nmessage: {request.POST['message']}")
        send_mail(
            subject=request.POST['subject'],
            message=organize,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS])
        return render(request, 'success.html')


@method_decorator(login_required, name='dispatch')
class ConfigPageView(UpdateView):
    template_name = 'config.html'
    fields = ('procfile_photo', 'cpf', 'name', 'email', 'cep', 'state', 'city', 'address', 'district', 'number', 'complement',)
    success_url = '/'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class AccountDelete(DeleteView):
    template_name = 'delete.html'
    success_url = '/'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class CancelPageView(TemplateView):
    template_name = 'cancel.html'


class SuccessPageView(TemplateView):
    template_name = 'order_success.html'


class FaQsPageView(ListView):
    queryset = FaQs.objects.all().order_by('-modified')
    context_object_name = 'faqs'
    template_name = 'faqs.html'


class PoliticPageView(ListView):
    context_object_name = 'politics'
    queryset = PoliticPage.objects.all().order_by('-modified')[0:1]
    template_name = 'politic.html'
