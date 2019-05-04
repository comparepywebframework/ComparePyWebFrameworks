import time
from functools import wraps
from .measurements import (
    record_external_api_call_time,
    get_last_json_serialization_record,
    get_last_external_api_call_record,
    get_last_inserted_to_database_record,
)
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


def get_last_json_serialization_execution_time(framework):
    record = get_last_json_serialization_record(framework=framework)
    if record is not None:
        return convert_to_miliseconds(record.execution_time)


def get_last_external_api_call_execution_time(framework):
    record = get_last_external_api_call_record(framework=framework)
    if record is not None:
        return convert_to_miliseconds(record.execution_time)


def get_last_inserted_to_database_execution_time(framework, number_of_inserted):
    record = get_last_inserted_to_database_record(framework=framework, number_of_inserted=number_of_inserted)
    if record is not None:
        return convert_to_miliseconds(record.execution_time)
