from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)

from .models import Image
from .forms import ImageUploadForm


def home(request):
    return render(request, 'photometa/base.html')


class ImageListView(LoginRequiredMixin, ListView):
    model = Image

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    form_class = ImageUploadForm
    success_url = reverse_lazy('photos')
    template_name = 'photometa/image_upload.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)
