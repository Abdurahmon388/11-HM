from django.urls import path

from . import views


from product.views import ProductListView, ProductDetailView

app_name = 'product'


urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('products/', views.product_list, name='product_list'),
]