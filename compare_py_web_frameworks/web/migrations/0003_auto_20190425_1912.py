# Generated by Django 2.1 on 2019-04-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190425_1904'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='insertingtodatabasemeasurement',
            table='web_inserting_to_database_measurement',
        ),
        migrations.AlterModelTable(
            name='renderingtemplatemeasurement',
            table='web_rendering_template_measurement',
        ),
    ]
