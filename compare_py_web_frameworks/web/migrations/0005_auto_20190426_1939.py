# Generated by Django 2.1 on 2019-04-26 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190426_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insertingtodatabasemeasurement',
            old_name='number_of_rendered',
            new_name='number_of_inserted',
        ),
    ]
