# Generated by Django 4.0.6 on 2022-07-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trecker', '0004_alter_task_types_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='trecker.type'),
        ),
    ]
