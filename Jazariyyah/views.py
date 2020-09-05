from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Jazariyyah
# Create your views here.


class JazariyyahList(ListView):
    model = Jazariyyah
    context_object_name = 'jazariyyah_content'
    template_name = 'jazariyyah.html'


class JazariyyahDetail(DetailView):
    model = Jazariyyah
    context_object_name = 'jazariyyah_content_detail'
    template_name = 'jazariyyah_detail.html'
