# Generated by Django 4.0.6 on 2022-08-12 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trecker', '0014_rename_users_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='User',
            field=models.ManyToManyField(default=1, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
