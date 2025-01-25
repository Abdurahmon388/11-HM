from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView

from . import forms
from pages import models
from .models import AboutModel


def main_page_view(request):
    return render(request,'index.html')

def home_page_view(request):

    if request.path == '/en/home/' or '/uz/home/':
        header_type = 'home_header'
    else:
        header_type = 'default_header'
    
    return render(request, 'pages/home.html', {'header_type': header_type})


def product_page_view(request):
    return render(request,'products/product.html')

def product_detail_page_view(request):
    return render(request,'products/product_detail.html')

class AboutPageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['posts'] = AboutModel.objects.all()
        return context

    template_name = 'pages/about.html'

def contact_page_view(request):

    if request.method == "POST":
        
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message save database')
            return redirect('pages:contact')

        else:
            messages.error(request,'Error')
            return redirect('pages:contact')

    else:
        return render(request,'pages/contact.html')