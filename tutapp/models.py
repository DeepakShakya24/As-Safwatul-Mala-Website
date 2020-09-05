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
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['pub_date']

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})


class Tajweed2(models.Model):
    user = models.ForeignKey(
        auth.models.User, on_delete=models.CASCADE, null=True)
    tajweed2_title = models.CharField(("Title"), max_length=200, null=True)
    tajweed2_audio_file = models.FileField(default='', blank=True)
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.tajweed2_title

    class Meta():
        ordering = ['pub_date']


class Tajweed3(models.Model):
    tajweed3_title = models.CharField(("Title"), max_length=200, null=True)
    tajweed3_audio_file = models.FileField(default='', blank=True)
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.tajweed3_title

    class Meta():
        ordering = ['pub_date']


class Advancetilawah(models.Model):
    tilawah_title = models.CharField(("Title"), max_length=200, null=True)
    tilawah_audio_file = models.FileField(default='', blank=True)
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.tilawah_title

    class Meta():
        ordering = ['pub_date']


class Jazariyyah(models.Model):
    jazariyyah_title = models.CharField(("Title"), max_length=200, null=True)
    jazariyaah_audio_file = models.FileField(default='', blank=True)
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.jazariyyah_title

    class Meta():
        ordering = ['pub_date']
