import time
from functools import wraps
from .measurements import record_external_api_call_time

def measure_execution_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        status = func(*args, **kwargs)
        end = time.time()
        return status, end - start
    return wrapped
