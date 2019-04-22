"""compare_py_web_frameworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from web import views

urlpatterns = [
    path('', views.index, name="index"),
    path('flask/', views.flask, name="flask"),
    path('django/', views.django, name="django"),
    path('render_flask_template/', views.render_flask_template, name="render_flask_template"),
    path('render_django_template/', views.render_django_template, name="render_django_template"),
    path('admin/', admin.site.urls),
]
