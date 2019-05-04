from django.shortcuts import render, redirect
import requests
import json
import time
from django.views.decorators.http import require_POST
from .error_messages import ErrorMessage, errors
from .helpers import (
    measure_template_rendering,
    measure_inserting_to_database,
    measure_external_api_call,
    measure_json_serialization,
)
from .measurements import (
    record_rendering_template_time,
    record_inserting_to_database_time,
    record_json_serialization_time,
    record_external_api_call_time,
    get_all_rendered_measurements_number,
    get_all_inserted_measurements_number,
    get_all_external_api_call_measurements_number,
    get_all_json_serialization_measurements_number,
)

from .measurement_helpers import (
    get_last_json_serialization_execution_time,
    get_last_external_api_call_execution_time,
    get_last_inserted_to_database_execution_time
)


def index(request):
    return render(request, "index.html")


def flask_info(request):
    return render(request, "flask.html")


def django_info(request):
    return render(request, "django.html")


def pyramid_info(request):
    return render(request, "pyramid.html")


def rendering_template(request):
    number_of_records_100 = get_all_rendered_measurements_number(number_of_rendered=100)
    number_of_records_1000 = get_all_rendered_measurements_number(
        number_of_rendered=1000
    )
    number_of_records_10000 = get_all_rendered_measurements_number(
        number_of_rendered=10000
    )
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "rendering_template.html",
            {
                "number_of_records_100": number_of_records_100,
                "number_of_records_1000": number_of_records_1000,
                "number_of_records_10000": number_of_records_10000,
                "error_message": ErrorMessage.CONNECTION_ERROR.value,
            },
        )
    return render(
        request,
        "rendering_template.html",
        {
            "number_of_records_100": number_of_records_100,
            "number_of_records_1000": number_of_records_1000,
            "number_of_records_10000": number_of_records_10000,
        },
    )


@require_POST
def record_rendering_template(request):
    django_status, execution_time_django = measure_template_rendering(
        request.POST["times"], request.POST["text"], "django"
    )
    flask_status, execution_time_flask = measure_template_rendering(
        request.POST["times"], request.POST["text"], "flask"
    )
    pyramid_status, execution_time_pyramid = measure_template_rendering(
        request.POST["times"], request.POST["text"], "pyramid"
    )
    if flask_status and django_status and pyramid_status:
        record_rendering_template_time(
            execution_time_django, "django", number_of_rendered=request.POST["times"]
        )
        record_rendering_template_time(
            execution_time_flask, "flask", number_of_rendered=request.POST["times"]
        )
        record_rendering_template_time(
            execution_time_pyramid, "pyramid", number_of_rendered=request.POST["times"]
        )
    else:
        request.session["error_message"] = True
    return redirect("rendering_template")


def inserting_to_database(request):
    number_of_records_10 = get_all_inserted_measurements_number(number_of_records=10)
    number_of_records_50 = get_all_inserted_measurements_number(number_of_records=50)
    number_of_records_100 = get_all_inserted_measurements_number(number_of_records=100)
    last_10_records_execution_time_flask = get_last_inserted_to_database_execution_time("flask", 10)
    last_10_records_execution_time_django = get_last_inserted_to_database_execution_time("django", 10)
    last_10_records_execution_time_pyramid = get_last_inserted_to_database_execution_time("pyramid", 10)
    last_50_records_execution_time_flask = get_last_inserted_to_database_execution_time("flask", 50)
    last_50_records_execution_time_django = get_last_inserted_to_database_execution_time("django", 50)
    last_50_records_execution_time_pyramid = get_last_inserted_to_database_execution_time("pyramid", 50)
    last_100_records_execution_time_flask = get_last_inserted_to_database_execution_time("flask", 100)
    last_100_records_execution_time_django = get_last_inserted_to_database_execution_time("django", 100)
    last_100_records_execution_time_pyramid = get_last_inserted_to_database_execution_time("pyramid", 100)
    measurements = {
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
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "inserting_to_database.html",
            {"measurements": measurements, "errors": errors },
        )
    return render(
        request, "inserting_to_database.html", {"measurements": measurements},)


@require_POST
def record_inserting_to_database(request):
    django_status, execution_time_django = measure_inserting_to_database(
        request.POST["times"], "django"
    )
    flask_status, execution_time_flask = measure_inserting_to_database(
        request.POST["times"], "flask"
    )
    pyramid_status, execution_time_pyramid = measure_inserting_to_database(
        request.POST["times"], "pyramid"
    )
    if django_status and flask_status and pyramid_status:
        record_inserting_to_database_time(
            execution_time_django, "django", number_of_inserted=request.POST["times"]
        )
        record_inserting_to_database_time(
            execution_time_flask, "flask", number_of_inserted=request.POST["times"]
        )
        record_inserting_to_database_time(
            execution_time_pyramid, "pyramid", number_of_inserted=request.POST["times"]
        )
    else:
        request.session["error_message"] = True
    return redirect("inserting_to_database")


def external_api_call(request):
    total_measurements = get_all_external_api_call_measurements_number()
    last_execution_time_flask = get_last_external_api_call_execution_time("flask")
    last_execution_time_django = get_last_external_api_call_execution_time("django")
    last_execution_time_pyramid = get_last_external_api_call_execution_time("pyramid")
    measurements = {
        "total_measurements": total_measurements,
        "last_execution_time_flask": last_execution_time_flask,
        "last_execution_time_django": last_execution_time_django,
        "last_execution_time_pyramid": last_execution_time_pyramid,
    }
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "external_api_call.html",
            {"measurements": measurements, "errors": errors},
        )
    return render(request, "external_api_call.html", {"measurements": measurements})


@require_POST
def record_external_api_call(request):
    flask_status, execution_time_flask = measure_external_api_call("flask")
    django_status, execution_time_django = measure_external_api_call("django")
    pyramid_status, execution_time_pyramid = measure_external_api_call("pyramid")
    if flask_status and django_status and pyramid_status:
        record_external_api_call_time(execution_time_flask, "flask")
        record_external_api_call_time(execution_time_django, "django")
        record_external_api_call_time(execution_time_pyramid, "pyramid")
    else:
        request.session["error_message"] = True
    return redirect("external_api_call")


def serialize_json(request):
    total_measurements = get_all_json_serialization_measurements_number()
    last_executon_time_django = get_last_json_serialization_execution_time("django")
    last_executon_time_flask = get_last_json_serialization_execution_time("flask")
    last_executon_time_pyramid = get_last_json_serialization_execution_time("pyramid")
    measurements = {
        "total_measurements": total_measurements,
        "last_execution_time_flask": last_executon_time_flask,
        "last_execution_time_django": last_executon_time_django,
        "last_execution_time_pyramid": last_executon_time_pyramid,
    }
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "serialize_json.html",
            {"measurements": measurements, "errors": errors},
        )
    return render(request, "serialize_json.html", {"measurements": measurements})


@require_POST
def record_json_serialization(request):
    flask_status, execution_time_flask = measure_json_serialization("flask")
    django_status, execution_time_django = measure_json_serialization("django")
    pyramid_status, execution_time_pyramid = measure_json_serialization("pyramid")
    if flask_status and django_status and pyramid_status:
        record_json_serialization_time(execution_time_flask, "flask")
        record_json_serialization_time(execution_time_django, "django")
        record_json_serialization_time(execution_time_pyramid, "pyramid")
    else:
        request.session["error_message"] = True
    return redirect("serialize_json")

