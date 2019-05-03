import time
import requests
from .measurements import record_external_api_call_time, record_json_serialization_time
from .measurement_helpers import measure_execution_time
import logging

logger = logging.getLogger(__name__)

DJANGO_SERVER_URL = "http://djangoframework:8001"
FLASK_SERVER_URL = "http://flask_framework:5000"
PYRAMID_SERVER_URL = "http://pyramid_framework:6543"


def get_server_url(framework):
    if framework == "django":
        return DJANGO_SERVER_URL
    elif framework == "flask":
        return FLASK_SERVER_URL
    else:
        return PYRAMID_SERVER_URL


@measure_execution_time
def measure_template_rendering(times, text, framework):
    server_url = get_server_url(framework)
    try:
        r = requests.post(server_url, json={"times": int(times), "text": text})
        if r.status_code == 200:
            logger.info(f"Render template msg sent to - {framework}")
            return True
    except Exception as e:
        logger.error(f"Rendering template connection error - {framework} - {e.message}")
        return False 


@measure_execution_time
def measure_inserting_to_database(times, framework):
    server_url = get_server_url(framework)
    try:
        r = requests.post(f"{server_url}/add_shop", json={"times": int(times)})
        if r.status_code == 201:
            logger.info(f"Insert data to database msg sent to - {framework}")
            r = requests.post(f"{server_url}/clear_shops_table")
            return True
    except Exception as e:
        logger.error(f"Inserting data to database connection error - {framework} - {e.message}")
        return False 


@measure_execution_time
def measure_external_api_call(framework):
    server_url = get_server_url(framework)
    start = time.time()
    try:
        r = requests.get(f"{server_url}/external_api_call")
        if r.status_code == 200:
            logger.info(f"External API call msg sent to - {framework}")
            return True
    except Exception as e:
        logger.error(f"External API Call connection error - {framework} = {e.message}")
        return False 


@measure_execution_time
def measure_json_serialization(framework):
    server_url = get_server_url(framework)
    try:
        r = requests.get(f"{server_url}/serialize_json")
        if r.status_code == 200:
            logger.info(f"Serialize JSON msg sent to - {framework}")
            return True
    except Exception as e:
        logger.error(f"JSON Serialization connection error - {framework} - {e.message}")
        return False

