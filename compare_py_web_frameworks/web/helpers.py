import time
import requests

DJANGO_SERVER_URL = "http://0.0.0.0:8001"
FLASK_SERVER_URL = "http://0.0.0.0:5000"
PYRAMID_SERVER_URL = "http://0.0.0.0:6543"


def render_django_template(request):
    start = time.time()
    try:
        r = requests.post(
            DJANGO_SERVER_URL,
            json={"times": int(request.POST["times"]), "text": request.POST["text"]},
        )
    except Exception:
        return "Connection error"
    end = time.time()
    return end - start


def render_flask_template(request):
    start = time.time()
    try:
        r = requests.post(
            FLASK_SERVER_URL,
            json={"times": int(request.POST["times"]), "text": request.POST["text"]},
        )
    except Exception:
        return "Connection error"
    end = time.time()
    return end - start


def render_pyramid_template(request):
    start = time.time()
    try:
        r = requests.post(
            PYRAMID_SERVER_URL,
            json={"times": int(request.POST["times"]), "text": request.POST["text"]},
        )
    except Exception:
        return "Connection error"
    end = time.time()
    return end - start


def insert_to_django_database(request):
    start = time.time()
    r = requests.post(
        f"{DJANGO_SERVER_URL}/add_shop", json={"times": int(request.POST["times"])}
    )
    if r.status_code == 201:
        end = time.time()
        r = requests.post(f"{DJANGO_SERVER_URL}/clear_shops_table")
    else:
        return "Error"
    return end - start


def insert_to_flask_database(request):
    start = time.time()
    r = requests.post(
        f"{FLASK_SERVER_URL}/add_shop", json={"times": int(request.POST["times"])}
    )
    if r.status_code == 201:
        end = time.time()
        r = requests.post(f"{FLASK_SERVER_URL}/clear_shops_table")
    else:
        return "Error"
    return end - start


def insert_to_pyramid_database(request):
    start = time.time()
    r = requests.post(
        f"{PYRAMID_SERVER_URL}/add_shop", json={"times": int(request.POST["times"])}
    )
    if r.status_code == 201:
        end = time.time()
        r = requests.post(f"{PYRAMID_SERVER_URL}/clear_shops_table")
    else:
        return "Error"
    return end - start