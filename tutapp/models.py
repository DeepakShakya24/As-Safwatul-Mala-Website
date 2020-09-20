from django.db import models
from django.urls import reverse
from django.contrib import auth

# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


class AudioClip(models.Model):
    title = models.CharField(("Title"), max_length=200, null=True)
    audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['id']


class Tajweed2(models.Model):
    tajweed2_title = models.CharField(("Title"), max_length=200, null=True)
    tajweed2_audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.tajweed2_title

    class Meta():
        ordering = ['id']


class Tajweed3(models.Model):
    tajweed3_title = models.CharField(("Title"), max_length=200, null=True)
    tajweed3_audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.tajweed3_title

    class Meta():
        ordering = ['id']


class Advancetilawah(models.Model):
    tilawah_title = models.CharField(("Title"), max_length=200, null=True)
    tilawah_audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.tilawah_title

    class Meta():
        ordering = ['id']


class Jazariyyah(models.Model):
    jazariyyah_title = models.CharField(("Title"), max_length=200, null=True)
    jazariyaah_audio_file = models.FileField(default='', blank=True)

    def __str__(self):
        return self.jazariyyah_title

    class Meta():
        ordering = ['id']
