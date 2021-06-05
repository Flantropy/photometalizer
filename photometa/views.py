from django.shortcuts import render, redirect
from users.models import Image
from .forms import ImageUploadForm
from users.models import Image


def home(request):
    return render(request, 'photometa/base.html')


def gallery(request):
    if request.method == 'POST':
        photo_upload_form = ImageUploadForm(
            request.POST,
            request.FILES,
            instance=Image.objects.create(profile=request.user.profile))
        if photo_upload_form.is_valid():
            photo_upload_form.save()
            return redirect('gallery')
    else:
        photo_upload_form = ImageUploadForm()

    user_photos = Image.objects.filter(profile__user__username=request.user)
    context = {
        'user_photos': user_photos,
        'photo_upload_form': photo_upload_form
    }
    return render(request, 'photometa/gallery.html', context)
