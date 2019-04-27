import time
import requests

DJANGO_SERVER_URL = "http://0.0.0.0:8001"
FLASK_SERVER_URL = "http://0.0.0.0:5000"
PYRAMID_SERVER_URL = "http://0.0.0.0:6543"


def get_server_url(framework):
    if framework == "django":
        return DJANGO_SERVER_URL
    elif framework == "flask":
        return FLASK_SERVER_URL
    else:
        return PYRAMID_SERVER_URL


def measure_template_rendering(request, framework):
    server_url = get_server_url(framework)
    start = time.time()
    try:
        r = requests.post(
            server_url,
            json={"times": int(request.POST["times"]), "text": request.POST["text"]},
        )
    except Exception:
        return "Connection Error"
    end = time.time()
    return end - start


def measure_inserting_to_database(request, framework):
    server_url = get_server_url(framework)
    start = time.time()
    try:
        r = requests.post(
            f"{server_url}/add_shop", json={"times": int(request.POST["times"])}
        )
        if r.status_code == 201:
            end = time.time()
            r = requests.post(f"{server_url}/clear_shops_table")
    except Exception:
        return "Connection Error"
    return round(end - start, 4)

