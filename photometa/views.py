from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)

from exif import Image as EXIFImage

from .forms import ImageUploadForm, ExifEditorForm
from .models import Image
from .utils import get_exif, safe_clear, write_image_with_new_meta


def home(request):
    return render(request, 'photometa/home.html')


def about(request):
    return render(request, 'photometa/about.html')


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
        files = self.request.FILES.getlist('img')
        for file in files:
            photo = Image(owner=self.request.user, img=file)
            photo.save()
        return redirect('photos')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return super().form_invalid(form)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('photos')

    def test_func(self):
        image = self.get_object()
        return self.request.user == image.owner


def image_meta(request, pk):
    obj = Image.objects.get(pk=pk)
    exif = get_exif(obj)
    context = {
        'photo': obj,
        'exif': exif.items()
    }
    return render(request, 'photometa/image_meta.html', context)


def image_meta_editor(request, pk):
    obj = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExifEditorForm(request.POST, request.FILES)
        if form.is_valid():
            image = EXIFImage(obj.img.read())
            for key, value in form.cleaned_data.items():
                if value:
                    image.set(key, value)

            write_image_with_new_meta(request, image)
            obj.delete()
            messages.success(request, '???????????? ?????????????? ??????????????????????????????')
            return redirect('photos')
    else:
        form = ExifEditorForm()
        initial_dirty = get_exif(obj)
        initial_cleaned = {k: v for k, v in initial_dirty.items() if k in form.declared_fields}
        form.initial = {**initial_cleaned}

    context = {
        'form': form,
    }
    return render(request, 'photometa/image_meta_editor.html', context)


def image_meta_clear(request, pk):
    try:
        obj = Image.objects.get(pk=pk)
        photo = obj.img.read()
        image = EXIFImage(photo)
        safe_clear(image)
        write_image_with_new_meta(request, image)
        obj.delete()
    except Exception as e:
        messages.warning(request, f'??????-???? ?????????? ???? ??????. {e.__class__}')
    else:
        messages.success(request, '???????????????????? ??????????????')
    return redirect('photos')


def delete_meta_for_all_user_photos(request):
    queryset = Image.objects.filter(owner=request.user)
    for i in queryset:
        photo = i.img.read()
        image = EXIFImage(photo)
        safe_clear(image)
        write_image_with_new_meta(request, image)
        i.delete()

    messages.success(request, '???????????????????? ?????????????? ???? ???????? ?????????? ????????')
    return redirect('photos')


def download(request, pk):
    obj = Image.objects.get(pk=pk)
    response = HttpResponse(obj.img.read(), content_type="file/force-download")
    response['Content-Disposition'] = f'inline; filename={obj.img}'
    return response
