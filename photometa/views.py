from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .forms import ImageUploadForm
from .models import Image


def home(request):
    return render(request, 'photometa/base.html')


def gallery(request):
    if request.method == 'POST':
        photo_upload_form = ImageUploadForm(
            request.POST,
            request.FILES,
            instance=Image.objects.create(owner=request.user))
        if photo_upload_form.is_valid():
            photo_upload_form.save()
            messages.success(request, f'Ваши фото успешно добавлены')
            return redirect('gallery')
    else:
        photo_upload_form = ImageUploadForm()

    user_photos = Image.objects.filter(owner=request.user)
    user_photos = [obj.img for obj in user_photos if obj.img]
    context = {
        'user_photos': user_photos,
        'photo_upload_form': photo_upload_form
    }
    return render(request, 'photometa/image_list.html', context)


class PhotoListView(ListView):
    model = Image
    queryset = Image.objects.all()
    extra_context = {
        'images': Image.objects.all()
    }


class PhotoDetailView(DetailView):
    model = Image
    template_name = 'photometa/photo_detail.html'
    context_object_name = 'photo'
