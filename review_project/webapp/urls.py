from django.contrib import admin
from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review_create_view'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update_view'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete_view'),

]
