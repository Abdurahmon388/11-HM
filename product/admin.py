from django.contrib import admin
from .models import Product
from .models import (
    ProductCategoryModel,
    ProductTagModel,
    ProductSizeModel,
    ProductManufactureModel,
    ProductColorModel,
    ProductModel,
    ProductCommentModel,
    ProductImageModel,
)

admin.site.register(Product)

@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)


@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(ProductSizeModel)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(ProductManufactureModel)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    search_fields = ('name',)


@admin.register(ProductColorModel)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'codo')
    search_fields = ('title', 'codo')


class ProductImageAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount', 'sku', 'in_stock', 'quantity')
    search_fields = ('title', 'sku')
    list_filter = ('in_stock', 'categories', 'brands')
    inlines = [ProductImageAdmin]


@admin.register(ProductCommentModel)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'comment')
    search_fields = ('comment', 'user__username', 'product__title')
    list_filter = ('product',)
