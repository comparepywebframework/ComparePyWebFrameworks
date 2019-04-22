from django.shortcuts import render, redirect
import requests
import json
import time
from .helpers import render_django_template, render_flask_template, DJANGO_SERVER_URL, FLASK_SERVER_URL, insert_to_django_database


def index(request):
    return render(request, 'index.html')


def rendering_template(request):
    if request.method == 'POST':
        execution_time_django = render_django_template(request)
        execution_time_flask = render_flask_template(request)
        return render(request, 'rendering_template.html', {'execution_time_django': execution_time_django, 'execution_time_flask': execution_time_flask})
    return render(request, 'rendering_template.html')


def inserting_to_database(request):
    if request.method == 'POST':
        execution_time_django = insert_to_django_database(request)
        return render(request, 'inserting_to_database.html', {'execution_time_django': execution_time_django})
    return render(request, 'inserting_to_database.html')