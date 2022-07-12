# Generated by Django 4.0.6 on 2022-07-12 11:07

from django.db import migrations



def transfer_types(apps, schema_editor):
    Task = apps.get_model('trecker.Task')
    for task in Task.objects.all():
        task.types.set(task.types_old.all())



def rollback_transfer(apps, schema_editor):
    Task = apps.get_model('trecker.Task')
    for task in Task.objects.all():
        task.types_old.set(task.types.all())


class Migration(migrations.Migration):

    dependencies = [
        ('trecker', '0005_task_types'),
    ]

    operations = [
        migrations.RunPython(transfer_types, rollback_transfer)
    ]