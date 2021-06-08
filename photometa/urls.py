from django.urls import path
from .views import (
    home,
    ImageListView,
    ImageDetailView,
    ImageCreateView,
    ImageDeleteView,
)


urlpatterns = [
    path('', home, name='home'),
    path('upload/', ImageCreateView.as_view(), name='photo-upload'),
    path('photos/', ImageListView.as_view(), name='photos'),
    path('photos/<int:pk>/', ImageDetailView.as_view(), name='photo-detail'),
    path('photos/<int:pk>/delete', ImageDeleteView.as_view(), name='photo-delete'),

]
