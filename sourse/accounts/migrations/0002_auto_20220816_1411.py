# Generated by Django 4.0.6 on 2022-08-16 08:11

from django.db import migrations

def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    for user in User.objects.filter(profile__isnull=True):
        Profile.objects.create(user=user)



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]
