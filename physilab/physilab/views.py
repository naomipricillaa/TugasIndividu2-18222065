from django.shortcuts import render, redirect

def index_page(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing.html')

def calc_page(request):
    return render(request, 'calc.html')

def material_page(request):
    return render(request, 'material.html')