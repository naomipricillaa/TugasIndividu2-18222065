from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile
from django.contrib.auth.views import LoginView


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Akun berhasil dibuat!")
            return redirect('login')
        else:
            messages.error(request, "Terjadi kesalahan. Mohon periksa kembali form.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Selamat datang, {user.username}!")
            return redirect('home')  # Update to the correct target home page
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, 'login.html')

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, "Username or password is incorrect or not registered.")
        return super().form_invalid(form)

def profile_view(request):
    return render(request, 'profile_view.html', {'user': request.user})

def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_view')  # Redirect back to the profile view page
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'profile_edit.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah keluar.")
    return redirect('index')  # Update to the desired logout redirect page
