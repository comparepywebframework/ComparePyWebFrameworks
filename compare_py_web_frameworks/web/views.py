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
)
from .contexts.external_api_call_context import get_external_api_call_measurements
from .contexts.database_context import get_database_measurements
from .contexts.serialize_json_context import get_serialize_json_measurements
from .contexts.render_template_context import get_render_template_measurements
from django.utils.translation import activate


def index(request):
    return render(request, "index.html")


def flask_info(request):
    return render(request, "flask.html")


def django_info(request):
    return render(request, "django.html")


def pyramid_info(request):
    return render(request, "pyramid.html")


def activate_pl_lang(request):
    activate("pl")
    return redirect("index")


def activate_en_lang(request):
    activate("en")
    return redirect("index")


def rendering_template(request):
    render_template_measurements = get_render_template_measurements()
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "rendering_template.html",
            {"measurements": render_template_measurements, "errors": errors},
        )
    return render(
        request,
        "rendering_template.html",
        {"measurements": render_template_measurements},
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
    database_measurements = get_database_measurements()
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "inserting_to_database.html",
            {"measurements": database_measurements, "errors": errors},
        )
    return render(
        request, "inserting_to_database.html", {"measurements": database_measurements}
    )


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
    external_api_call_measurements = get_external_api_call_measurements()
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "external_api_call.html",
            {"measurements": external_api_call_measurements, "errors": errors},
        )
    return render(
        request,
        "external_api_call.html",
        {"measurements": external_api_call_measurements},
    )


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
    serialize_json_measurements = get_serialize_json_measurements()
    if request.session.get("error_message", False):
        request.session["error_message"] = False
        return render(
            request,
            "serialize_json.html",
            {"measurements": serialize_json_measurements, "errors": errors},
        )
    return render(
        request, "serialize_json.html", {"measurements": serialize_json_measurements}
    )


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

