# Generated by Django 4.0.5 on 2022-06-09 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='fechaInicio',
        ),
    ]
