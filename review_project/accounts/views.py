from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreateForm, UserChangeForm, PasswordChangeForm

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


class UserProfileView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_object"

    def get_context_data(self, **kwargs):
        reviews = self.object.reviews.all()
        kwargs['reviews'] = reviews
        return super().get_context_data(**kwargs)


class UserChangeUpdateView(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'profile_update.html'

    def has_permission(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_object'

    def has_permission(self):
        return self.request.user == self.get_object()

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})

