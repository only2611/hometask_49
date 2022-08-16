from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Аватар")
    git_link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Профиль на Github")
    yourself = models.TextField(max_length=500, null=True, blank=True, verbose_name="О себе")
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name="Юзер", related_name="profile")