from django.shortcuts import render, redirect
import requests
import json
import time


def index(request):
    return render(request, 'index.html')


def flask(request):
    return render(request, 'flask.html')


def render_flask_template(request):
    start = time.time()
    r = requests.post('http://0.0.0.0:5000',
                      json={"times": int(request.POST['times']), "text": request.POST['text']})
    rendered_template = r.text
    end = time.time()
    execution_time = end - start
    return render(request, 'flask.html', {'execution_time': execution_time, 'rendered_template': rendered_template})


def django(request):
    return render(request, 'django.html')


def render_django_template(request):
    start = time.time()
    r = requests.post('http://0.0.0.0:8001',
                      json={"times": int(request.POST['times']), "text": request.POST['text']})
    rendered_template = r.text
    end = time.time()
    execution_time = end - start
    return render(request, 'django.html', {'execution_time': execution_time, 'rendered_template': rendered_template})
