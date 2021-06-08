from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'pk': self.pk})