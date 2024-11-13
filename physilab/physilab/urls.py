from django.contrib import admin
from django.urls import path, include
from .views import index_page, landing_page, material_page
from calculator import views as calculator_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', index_page, name='index_page'),
    path('landing/', landing_page, name='landing_page'),
    path('calc/', calculator_views.calculate_pressure, name='calc'),
    path('material/', material_page, name='material'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
