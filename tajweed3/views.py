from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Tajweed3
# Create your views here.


class Tajweed3List(ListView):
    model = Tajweed3
    context_object_name = 'tajweed3_content'
    template_name = 'Course3.html'


class Tajweed3Detail(DetailView):
    model = Tajweed3
    context_object_name = 'tajweed3_content_detail'
    template_name = 'Course3detail.html'
