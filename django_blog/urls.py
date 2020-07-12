"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django_blog import settings
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up', users_views.sign_up, name='sign_up'),
    path('sign_in', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign_in'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='log_out'),
    path('profile', users_views.profile, name='profile'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


