from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from exif import Image as EXIFImage
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
        return super().form_valid(form)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('photos')

    def test_func(self):
        image = self.get_object()
        return self.request.user == image.owner


def image_meta(request, pk):
    obj = Image.objects.get(pk=pk)
    photo = obj.img.read()
    photo_raw_exif = EXIFImage(photo)
    exif = photo_raw_exif.get_all()
    exif = zip(exif.keys(), exif.values())
    context = {
        'photo': photo,
        'mypk': pk,
        'exif': exif,
    }
    return render(request, 'photometa/image_meta.html', context)


def image_meta_editor(request, pk):
    obj = Image.objects.get(pk=pk)
    photo = obj.img.read()
    photo_raw_exif = EXIFImage(photo)
    exif = photo_raw_exif.get_all()
    exif = zip(exif.keys(), exif.values())
    context = {
        'all_tags': exif,
    }
    return render(request, 'photometa/image_meta_editor.html', context)


def image_meta_clear(request, pk):
    try:
        obj = Image.objects.get(pk=pk)
        photo = obj.img.read()
        image = EXIFImage(photo)
        image.delete_all()
        new_file = image.get_file()
        new_obj = Image()
        new_obj.owner = request.user
        new_obj.img.save(name='new_image.jpg', content=ContentFile(new_file))
        new_obj.save()
        obj.delete()
    except:
        messages.error(request, 'Error')
    messages.success(request, 'Метаданные удалены')
    return redirect('photos')
