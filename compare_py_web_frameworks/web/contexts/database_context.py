from web.measurements import (
    record_inserting_to_database_time,
    get_all_inserted_measurements_number,
)

from web.measurement_helpers import get_last_inserted_to_database_execution_time


def get_database_measurements():
    number_of_records_10 = get_all_inserted_measurements_number(number_of_records=10)
    number_of_records_50 = get_all_inserted_measurements_number(number_of_records=50)
    number_of_records_100 = get_all_inserted_measurements_number(number_of_records=100)
    last_10_records_execution_time_flask = get_last_inserted_to_database_execution_time(
        "flask", 10
    )
    last_10_records_execution_time_django = get_last_inserted_to_database_execution_time(
        "django", 10
    )
    last_10_records_execution_time_pyramid = get_last_inserted_to_database_execution_time(
        "pyramid", 10
    )
    last_50_records_execution_time_flask = get_last_inserted_to_database_execution_time(
        "flask", 50
    )
    last_50_records_execution_time_django = get_last_inserted_to_database_execution_time(
        "django", 50
    )
    last_50_records_execution_time_pyramid = get_last_inserted_to_database_execution_time(
        "pyramid", 50
    )
    last_100_records_execution_time_flask = get_last_inserted_to_database_execution_time(
        "flask", 100
    )
    last_100_records_execution_time_django = get_last_inserted_to_database_execution_time(
        "django", 100
    )
    last_100_records_execution_time_pyramid = get_last_inserted_to_database_execution_time(
        "pyramid", 100
    )

    return {
        "number_of_records_10": number_of_records_10,
        "number_of_records_50": number_of_records_50,
        "number_of_records_100": number_of_records_100,
        "last_10_records_execution_time_flask": last_10_records_execution_time_flask,
        "last_10_records_execution_time_django": last_10_records_execution_time_django,
        "last_10_records_execution_time_pyramid": last_10_records_execution_time_pyramid,
        "last_50_records_execution_time_flask": last_50_records_execution_time_flask,
        "last_50_records_execution_time_django": last_50_records_execution_time_django,
        "last_50_records_execution_time_pyramid": last_50_records_execution_time_pyramid,
        "last_100_records_execution_time_flask": last_100_records_execution_time_flask,
        "last_100_records_execution_time_django": last_100_records_execution_time_django,
        "last_100_records_execution_time_pyramid": last_100_records_execution_time_pyramid,
    }

