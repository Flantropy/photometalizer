from django.contrib import messages
from django.shortcuts import render, redirect
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


class ImageListView(ListView):
    model = Image

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    form_class = ImageUploadForm


class ImageDeleteView(DeleteView):
    pass
