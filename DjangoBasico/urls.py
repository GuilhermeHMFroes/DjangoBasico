"""
URL configuration for DjangoBasico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views

urlpatterns = [

    path('paineldecontrole/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('w3c/', views.w3c, name='w3c'),
    path('formulario/', views.formulario, name='formulario'),
    path('HTML', views.HTML, name='HTML'),
    path('CSS', views.CSS, name='CSS'),
    path('JavaScript', views.JavaScript, name='JavaScript'),
    path('Frontend', views.Frontend, name='Frontend'),
    path('Backend', views.Backend, name='Backend'),

]
