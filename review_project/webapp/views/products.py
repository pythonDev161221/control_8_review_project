from django.views.generic import ListView

from webapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list_view.html"
    context_object_name = 'products'
