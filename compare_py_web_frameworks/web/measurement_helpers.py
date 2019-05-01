import time


def measure_execution_time(func):
    def f(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return f
