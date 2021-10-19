from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CostumerUser(AbstractUser):
    sexo = models.CharField(max_length=15, blank=True, null=True, default=None)
    biografia = models.TextField(blank=True)
    imagem = models.ImageField(blank=True, upload_to='fotoPerfil')

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)