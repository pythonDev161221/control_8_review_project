from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list_view.html"
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail_view.html"

    def get_context_data(self, **kwargs):
        reviews = self.object.reviews.filter(is_moderated__exact=True)
        kwargs['reviews'] = reviews
        return super().get_context_data(**kwargs)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = "products/product_create_view.html"
    form_class = ProductForm
    permission_required = 'webapp.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "products/product_update_view.html"
    form_class = ProductForm
    permission_required = 'webapp.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "products/product_delete_view.html"
    success_url = reverse_lazy('webapp:product_list_view')
    permission_required = 'webapp.delete_product'

