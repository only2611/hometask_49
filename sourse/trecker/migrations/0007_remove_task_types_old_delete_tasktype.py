# Generated by Django 4.0.6 on 2022-07-12 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecker', '0006_auto_20220712_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='types_old',
        ),
        migrations.DeleteModel(
            name='TaskType',
        ),
    ]