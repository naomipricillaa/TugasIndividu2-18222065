from django.contrib import admin
from django.urls import path, include
from .views import index_page, landing_page, material_page
from calculator import views as calculator_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # User authentication paths
    path('signup/', user_views.signup_view, name='signup'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.profile_view, name='profile_view'),  # Use user_views here
    path('profile/edit/', user_views.profile_edit, name='profile_edit'),  # Use user_views here

    # Main application paths
    path('', index_page, name='index_page'),
    path('landing/', views.landing_page, name='landing_page'),
    path('calc/', calculator_views.calculate_pressure, name='calc'),
    path('clear_history/', calculator_views.clear_history, name='clear_history'),
    path('material/', material_page, name='material'),

    # Include other urls from the 'users' app if there are additional routes
    path('users/', include('users.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
