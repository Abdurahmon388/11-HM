from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/',views.contact_page_view,name='contact'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('product/',views.product_page_view,name='product'),
    path('product/product-detail',views.product_detail_page_view,name='product_detail'),
    path('home/',views.home_page_view,name='home'),
    path('',views.main_page_view,name='main')
]