from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_create_view.html"

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        review.product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review.is_moderated = False
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail_view', kwargs={'pk': self.kwargs.get('pk')})


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_update_view.html"
    permission_required = "webapp.change_review"

    def get_success_url(self):
        return reverse('webapp:product_detail_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review_delete_view.html"
    permission_required = "webapp.delete_review"

    def get_success_url(self):
        return reverse('webapp:product_detail_view', kwargs={'pk': self.object.product.pk})