from django.db.models.expressions import result
from django.views.generic import TemplateView

from django.views.generic import ListView

from product.models import *

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Barcha ma'lumotlarni olish
    return render(request, 'product_list.html', {'products': products})

class ProductListView(ListView):
    model = ProductModel
    template_name = 'products/product.html'
    context_object_name = 'products'
    paginate_by = 1




    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["colors"] = self.make_color_groups()
        context["categories"] = ProductCategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["brands"] = ProductManufactureModel.objects.all()
        context["sizes"] = ProductSizeModel.objects.all()
        return context

    @staticmethod
    def make_color_groups():
        colors = ProductColorModel.objects.all()
        print(colors)
        result = list()
        temp_list = list()
        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []

        if len(temp_list) >= 1:
            result.append(temp_list)

        return result


class ProductDetailView(TemplateView):
    template_name = 'products/product_detail.html'

# Create your views here.
