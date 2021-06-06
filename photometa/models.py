from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')
