"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views

urlpatterns = [
        # раздел администратора
        path('admin/', admin.site.urls),
        # flatpages
        path('about/', include('django.contrib.flatpages.urls')),
        # регистрация и авторизация
        path('auth/', include('users.urls')),
        path('auth/', include('django.contrib.auth.urls')),
        # импорт из приложения posts
        path('', include('posts.urls')),
        path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about-author'),
        path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='about-spec')
        # path('about-author/', include('django.contrib.flatpages.urls')),
        # path('about-spec/', include('django.contrib.flatpages.urls')),
]

# добавим новые пути
# urlpatterns += [
#         path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about-author'),
#         path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='about-spec')
# ]
