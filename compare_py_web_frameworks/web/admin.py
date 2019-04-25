from django.contrib import admin
from .models import RenderingTemplateMeasurement, InsertingToDatabaseMeasurement


admin.site.register(RenderingTemplateMeasurement)
admin.site.register(InsertingToDatabaseMeasurement)
