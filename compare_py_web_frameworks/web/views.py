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
    r = requests.post('http://0.0.0.0:5000', json={"times": request.POST['times'], "text": request.POST['text']})
    r.text
    end = time.time()
    execution_time = end - start
    return render(request, 'flask.html', {'execution_time': execution_time})
    