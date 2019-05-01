from .models import (
    RenderingTemplateMeasurement,
    InsertingToDatabaseMeasurement,
    ExternalApiCallMeasurement,
    JSONSerializationMeasurement,
)


def record_rendering_template_time(execution_time, framework, number_of_rendered):
    try:
        RenderingTemplateMeasurement.objects.create(
            execution_time=execution_time,
            framework=framework,
            number_of_rendered=number_of_rendered,
        )
    except Exception:
        return False
    return True


def record_inserting_to_database_time(execution_time, framework, number_of_inserted):
    try:
        InsertingToDatabaseMeasurement.objects.create(
            execution_time=execution_time,
            framework=framework,
            number_of_inserted=number_of_inserted,
        )
    except Exception:
        return False
    return True


def record_external_api_call_time(execution_time, framework):
    try:
        ExternalApiCallMeasurement.objects.create(
            execution_time=execution_time, framework=framework
        )
    except Exception:
        return False
    return True


def record_json_serialization_time(execution_time, framework):
    try:
        JSONSerializationMeasurement.objects.create(execution_time=execution_time, framework=framework)
    except Exception:
        return False
    return True



def get_all_rendered_measurements_number(number_of_rendered):
    return RenderingTemplateMeasurement.objects.filter(
        number_of_rendered=number_of_rendered, framework="django"
    ).count()


def get_all_inserted_measurements_number(number_of_records):
    return InsertingToDatabaseMeasurement.objects.filter(
        number_of_inserted=number_of_records, framework="django"
    ).count()


def get_all_external_api_call_measurements_number():
    return ExternalApiCallMeasurement.objects.filter(framework="django").count()


def get_all_json_serialization_measurements_number():
    return JSONSerializationMeasurement.objects.filter(framework="django").count()