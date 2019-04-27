from django.db import models


class RenderingTemplateMeasurement(models.Model):

    class Meta:
        db_table = 'web_rendering_template_measurement'

    date = models.DateTimeField(auto_now=True)
    execution_time = models.FloatField()
    framework = models.CharField(max_length=20)
    number_of_rendered = models.IntegerField()

    def __str__(self):
        return f"{self.framework} - {self.execution_time}"


class InsertingToDatabaseMeasurement(models.Model):

    class Meta:
        db_table = 'web_inserting_to_database_measurement'

    date = models.DateTimeField(auto_now=True)
    execution_time = models.FloatField()
    framework = models.CharField(max_length=20)
    number_of_inserted = models.IntegerField() 

    def __str__(self):
        return f"{self.framework} - {self.execution_time}"
        

