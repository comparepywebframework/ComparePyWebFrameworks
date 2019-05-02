from django.shortcuts import render, redirect
import requests
import json
import time
from django.views.decorators.http import require_POST
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
    execution_time_django = measure_template_rendering(
        request.POST["times"], request.POST["text"], "django"
    )
    execution_time_flask = measure_template_rendering(
        request.POST["times"], request.POST["text"], "flask"
    )
    execution_time_pyramid = measure_template_rendering(
        request.POST["times"], request.POST["text"], "pyramid"
    )
    record_rendering_template_time(
        execution_time=execution_time_django,
        framework="django",
        number_of_rendered=request.POST["times"],
    )
    record_rendering_template_time(
        execution_time=execution_time_flask,
        framework="flask",
        number_of_rendered=request.POST["times"],
    )
    record_rendering_template_time(
        execution_time=execution_time_pyramid,
        framework="pyramid",
        number_of_rendered=request.POST["times"],
    )
    return redirect("rendering_template")


def inserting_to_database(request):
    number_of_records_10 = get_all_inserted_measurements_number(number_of_records=10)
    number_of_records_50 = get_all_inserted_measurements_number(number_of_records=50)
    number_of_records_100 = get_all_inserted_measurements_number(number_of_records=100)
    return render(
        request,
        "inserting_to_database.html",
        {
            "number_of_records_10": number_of_records_10,
            "number_of_records_50": number_of_records_50,
            "number_of_records_100": number_of_records_100,
        },
    )


@require_POST
def record_inserting_to_database(request):
    execution_time_django = measure_inserting_to_database(
        request.POST["times"], "django"
    )
    execution_time_flask = measure_inserting_to_database(request.POST["times"], "flask")
    execution_time_pyramid = measure_inserting_to_database(
        request.POST["times"], "pyramid"
    )
    record_inserting_to_database_time(
        execution_time_django,
        framework="django",
        number_of_inserted=request.POST["times"],
    )
    record_inserting_to_database_time(
        execution_time_flask,
        framework="flask",
        number_of_inserted=request.POST["times"],
    )
    record_inserting_to_database_time(
        execution_time_pyramid,
        framework="pyramid",
        number_of_inserted=request.POST["times"],
    )
    return redirect("inserting_to_database")


def external_api_call(request):
    total_measurements = get_all_external_api_call_measurements_number()
    return render(
        request, "external_api_call.html", {"total_measurements": total_measurements}
    )


@require_POST
def record_external_api_call(request):
    execution_time = measure_external_api_call("flask")
    record_external_api_call_time(execution_time=execution_time, framework="flask")
    execution_time = measure_external_api_call("django")
    record_external_api_call_time(execution_time=execution_time, framework="django")
    execution_time = measure_external_api_call("pyramid")
    record_external_api_call_time(execution_time=execution_time, framework="pyramid")
    return redirect("external_api_call")


def serialize_json(request):
    total_measurements = get_all_json_serialization_measurements_number()
    return render(
        request, "serialize_json.html", {"total_measurements": total_measurements}
    )


@require_POST
def record_json_serialization(request):
    execution_time = measure_json_serialization("flask")
    record_json_serialization_time(execution_time, "flask")
    execution_time = measure_json_serialization("django")
    record_json_serialization_time(execution_time, "django")
    execution_time = measure_json_serialization("pyramid")
    record_json_serialization_time(execution_time, "pyramid")
    return redirect("serialize_json")

