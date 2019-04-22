import time
import requests

DJANGO_SERVER_URL = 'http://0.0.0.0:8001'
FLASK_SERVER_URL = 'http://0.0.0.0:5000'

def render_django_template(request):
    start = time.time()
    r = requests.post(DJANGO_SERVER_URL,
                      json={"times": int(request.POST['times']), "text": request.POST['text']})
    end = time.time()
    execution_time = end - start
    return execution_time


def render_flask_template(request):
    start = time.time()
    r = requests.post(FLASK_SERVER_URL,
                      json={"times": int(request.POST['times']), "text": request.POST['text']})
    end = time.time()
    execution_time = end - start
    return execution_time


def insert_to_django_database(request):
    start = time.time()
    r = requests.post(f'{DJANGO_SERVER_URL}/add_shop',
                      json={'times': int(request.POST['times'])})
    if r.status_code == 201:
        end = time.time()
        execution_time = end - start
        r = requests.post(f'{DJANGO_SERVER_URL}/clear_shops_table')
    else:
        return 'Error'
    return execution_time