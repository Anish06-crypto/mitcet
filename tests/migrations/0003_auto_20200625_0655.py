# Generated by Django 3.0.6 on 2020-06-25 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_studenttest_started_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttest',
            old_name='started_at',
            new_name='end_at',
        ),
    ]
