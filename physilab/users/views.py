from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Akun berhasil dibuat!")
            return redirect('login')  # Pastikan ada URL 'login'
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
            return redirect('home')  # Update to the target home page
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, 'login.html')
