from django.contrib import admin
from .models import AudioClip, Tajweed2, Tajweed3, Advancetilawah, Jazariyyah

import os.path
# Register your models here.
admin.site.register(AudioClip)
admin.site.register(Tajweed2)
admin.site.register(Tajweed3)
admin.site.register(Advancetilawah)
admin.site.register(Jazariyyah)
