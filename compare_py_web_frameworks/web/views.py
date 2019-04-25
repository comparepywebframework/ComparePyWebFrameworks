from django.shortcuts import render, redirect
import requests
import json
import time
from .helpers import (
    render_django_template,
    render_flask_template,
    DJANGO_SERVER_URL,
    FLASK_SERVER_URL,
    insert_to_django_database,
    insert_to_flask_database,
    render_pyramid_template,
    insert_to_pyramid_database,
)
from .measurements import record_rendering_template_time


def index(request):
    return render(request, "index.html")


def rendering_template(request):
    if request.method == "POST":
        execution_time_django = render_django_template(request)
        execution_time_flask = render_flask_template(request)
        execution_time_pyramid = render_pyramid_template(request)
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
        return render(
            request,
            "rendering_template.html",
            {
                "execution_time_django": execution_time_django,
                "execution_time_flask": execution_time_flask,
                "execution_time_pyramid": execution_time_pyramid,
            },
        )
    return render(request, "rendering_template.html")


def inserting_to_database(request):
    if request.method == "POST":
        execution_time_django = insert_to_django_database(request)
        execution_time_flask = insert_to_flask_database(request)
        execution_time_pyramid = insert_to_pyramid_database(request)
        return render(
            request,
            "inserting_to_database.html",
            {
                "execution_time_django": execution_time_django,
                "execution_time_flask": execution_time_flask,
                "execution_time_pyramid": execution_time_pyramid,
            },
        )
    return render(request, "inserting_to_database.html")
