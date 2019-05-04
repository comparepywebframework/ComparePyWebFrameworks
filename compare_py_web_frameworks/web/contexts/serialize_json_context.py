from web.measurements import get_all_json_serialization_measurements_number

from web.measurement_helpers import get_last_json_serialization_execution_time


def get_serialize_json_measurements():
    total_measurements = get_all_json_serialization_measurements_number()
    last_executon_time_django = get_last_json_serialization_execution_time("django")
    last_executon_time_flask = get_last_json_serialization_execution_time("flask")
    last_executon_time_pyramid = get_last_json_serialization_execution_time("pyramid")
    return {
        "total_measurements": total_measurements,
        "last_execution_time_flask": last_executon_time_flask,
        "last_execution_time_django": last_executon_time_django,
        "last_execution_time_pyramid": last_executon_time_pyramid,
    }
