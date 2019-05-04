import time
from functools import wraps
from .measurements import record_external_api_call_time, get_last_json_serialization_record
import statistics

def convert_to_miliseconds(time):
    return round(time * 1000, 2)


def measure_execution_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        status = func(*args, **kwargs)
        end = time.time()
        return status, end - start
    return wrapped


def get_last_execution_time(framework):
    record = get_last_json_serialization_record(framework=framework)
    return convert_to_miliseconds(record.execution_time)


