from web.measurements import get_all_rendered_measurements_number

from web.measurement_helpers import get_last_rendered_template_execution_time


def get_render_template_measurements():
    number_of_records_100 = get_all_rendered_measurements_number(number_of_rendered=100)
    number_of_records_1000 = get_all_rendered_measurements_number(
        number_of_rendered=1000
    )
    number_of_records_10000 = get_all_rendered_measurements_number(
        number_of_rendered=10000
    )
    last_100_execution_time_flask = get_last_rendered_template_execution_time(
        "flask", 100
    )
    last_100_execution_time_django = get_last_rendered_template_execution_time(
        "django", 100
    )
    last_100_execution_time_pyramid = get_last_rendered_template_execution_time(
        "pyramid", 100
    )
    last_10000_execution_time_flask = get_last_rendered_template_execution_time(
        "flask", 1000
    )
    last_1000_execution_time_django = get_last_rendered_template_execution_time(
        "django", 1000
    )
    last_1000_execution_time_pyramid = get_last_rendered_template_execution_time(
        "pyramid", 1000
    )
    last_10000_execution_time_flask = get_last_rendered_template_execution_time(
        "flask", 10000
    )
    last_10000_execution_time_django = get_last_rendered_template_execution_time(
        "django", 10000
    )
    last_10000_execution_time_pyramid = get_last_rendered_template_execution_time(
        "pyramid", 10000
    )

    return {
        "number_of_records_100": number_of_records_100,
        "number_of_records_1000": number_of_records_1000,
        "number_of_records_10000": number_of_records_10000,
        "last_100_execution_time_flask": last_100_execution_time_flask,
        "last_100_execution_time_django": last_100_execution_time_django,
        "last_100_execution_time_pyramid": last_100_execution_time_pyramid,
        "last_1000_execution_time_flask": last_10000_execution_time_flask,
        "last_1000_execution_time_django": last_1000_execution_time_django,
        "last_1000_execution_time_pyramid": last_1000_execution_time_pyramid,
        "last_10000_execution_time_flask": last_10000_execution_time_flask,
        "last_10000_execution_time_django": last_10000_execution_time_django,
        "last_10000_execution_time_pyramid": last_10000_execution_time_pyramid,
    }
