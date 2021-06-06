from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' {username}, ваш аккаунт успешно создан.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form })


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f'Ваш профиль обновлен')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)

    context = {
        'user_update_form': user_update_form,
    }
    return render(request, 'users/profile.html', context)
