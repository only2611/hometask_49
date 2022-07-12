# Generated by Django 4.0.6 on 2022-07-12 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trecker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='tasks', through='trecker.TaskType', to='trecker.type'),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_types', to='trecker.task', verbose_name='Задача'),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_tasks', to='trecker.type', verbose_name='Тип'),
        ),
    ]
