import os

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    FormView
)

from .models import Image
from .forms import ImageUploadForm
from .utils import retrieve_exif, clear_meta


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
        return super().form_valid(form)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('photos')

    def test_func(self):
        image = self.get_object()
        return self.request.user == image.owner


def image_meta(request, pk):
    photo = Image.objects.get(pk=pk)
    exif = retrieve_exif(photo.img.path)
    context = {
        'photo': photo,
        'mypk': pk,
        'exif': exif,
    }
    return render(request, 'photometa/image_meta.html', context)


def image_meta_editor(request, pk):
    photo = Image.objects.get(pk=pk)
    exif = retrieve_exif(photo.img.path)
    context = {
        'all_tags': exif,
    }
    return render(request, 'photometa/image_meta_editor.html', context)


def image_meta_clear(request, pk):
    photo = Image.objects.get(pk=pk)
    try:
        clear_meta(photo.img.path)
    except:
        messages.error(request, f'Что-то пошло не так')
    messages.success(request, f'Метаданные для {photo} удалены')
    return redirect('photos')
