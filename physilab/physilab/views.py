from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index_page(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing.html')

def calc_page(request):
    return render(request, 'calc.html')

def material_page(request):
    return render(request, 'material.html')