from django.contrib import admin
from django.urls import path

from webapp.views import ProductListView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),

]
