from django.views.generic import ListView, DetailView

from webapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list_view.html"
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail_view.html"