from web.measurements import get_all_external_api_call_measurements_number

from web.measurement_helpers import get_last_external_api_call_execution_time


def get_external_api_call_measurements():
    total_measurements = get_all_external_api_call_measurements_number()
    last_execution_time_flask = get_last_external_api_call_execution_time("flask")
    last_execution_time_django = get_last_external_api_call_execution_time("django")
    last_execution_time_pyramid = get_last_external_api_call_execution_time("pyramid")
    return {
        "total_measurements": total_measurements,
        "last_execution_time_flask": last_execution_time_flask,
        "last_execution_time_django": last_execution_time_django,
        "last_execution_time_pyramid": last_execution_time_pyramid,
    }
