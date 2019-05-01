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
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', views.index, name="index"),
    path('rendering_template/', views.rendering_template, name="rendering_template"),
    path('record_rendering_template/', views.record_rendering_template, name="record_rendering_template"),
    path('insertinng_to_database/', views.inserting_to_database, name="inserting_to_database"),
    path('record_inserting_to_database/', views.record_inserting_to_database, name="record_inserting_to_database"),
    path('external_api_call/', views.external_api_call, name="external_api_call"),
    path('record_external_api_call/', views.record_external_api_call, name="record_external_api_call"),
    path('serialize_json/', views.serialize_json, name="serialize_json"),
    path('record_json_serialization/', views.record_json_serialization, name="record_json_serialization"),
)
