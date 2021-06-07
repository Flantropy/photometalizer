from django.urls import path
from .views import home, PhotoDetailView, PhotoListView


urlpatterns = [
    path('', home, name='home'),
    path('photos/', PhotoListView.as_view(), name='photos'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail')
]
