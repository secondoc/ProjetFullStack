"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("<int:id>", views.searchid),
    path("connexion/", views.connexion, name='connexion'),
    path("deconnexion/", views.deconnexion, name='deconnexion'),
    path("register/", views.register, name='register'),
    path("articles/", views.articles, name='articles'),
    path('article/<int:id>', views.lire, name='lire'),
    path('fav/<int:id>', views.ajout_fav, name='ajout_fav'),
    path('favoris/', views.liste_fav, name='liste_fav'),
    path('search', views.search, name='search')
    
]
