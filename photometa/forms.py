from django import forms
from users.models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['img']
