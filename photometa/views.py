from django.contrib import messages
from django.shortcuts import render, redirect
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
    user_photos_urls = [obj.img.url for obj in user_photos]
    context = {
        'user_photos_urls': user_photos_urls,
        'photo_upload_form': photo_upload_form
    }
    return render(request, 'photometa/gallery.html', context)
