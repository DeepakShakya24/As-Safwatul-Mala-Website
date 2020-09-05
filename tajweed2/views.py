from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Tajweed2
# Create your views here.


class Tajweed2List(ListView):
    model = Tajweed2
    context_object_name = 'tajweed2_content'
    template_name = 'Course2.html'


class Tajweed2Detail(DetailView):
    model = Tajweed2
    context_object_name = 'tajweed2_content_detail'
    template_name = 'Course2detail.html'
