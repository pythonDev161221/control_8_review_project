from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import MyUserCreateForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreateForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:product_list_view")