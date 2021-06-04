from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from users import views as user_views


urlpatterns = [
    path('', include('photometa.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path(
      'login/',
      LoginView.as_view(template_name='users/login.html'),
      name='login'
    ),
    path(
      'logout/',
      LogoutView.as_view(template_name='users/logout.html'),
      name='logout'
    ),
    path(
      'password-reset/',
      PasswordResetView.as_view(template_name='users/password_reset.html'),
      name='password_reset'
    ),
    path(
      'password-reset/done/',
      PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
      name='password_reset_done'
    ),
    path(
      'password-reset-confirm/<uidb64>/<token>/',
      PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
      name='password_reset_confirm'
    ),
    path(
      'password-reset-complete/',
      PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
      name='password_reset_complete'
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media root has to be set
