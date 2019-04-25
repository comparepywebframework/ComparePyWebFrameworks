from .models import RenderingTemplateMeasurement, InsertingToDatabaseMeasurement

def record_rendering_template_time(execution_time, framework, number_of_rendered):
    try:
        RenderingTemplateMeasurement.objects.create(execution_time=execution_time, framework=framework, number_of_rendered=number_of_rendered)
    except Exception:
        return False
    return True

