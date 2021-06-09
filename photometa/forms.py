from django.forms import Form, ModelForm
from django.forms.fields import *
from .models import Image



class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['img']


class ExifEditorForm(Form):
    title = CharField()
    email = EmailField()
