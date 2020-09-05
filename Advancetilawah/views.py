from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Advancetilawah
# Create your views here.


class AdvancetilawahList(ListView):
    model = Advancetilawah
    context_object_name = 'tilawah_content'
    template_name = 'Advance Tilawah.html'


class AdvancetilawahDetail(DetailView):
    model = Advancetilawah
    context_object_name = 'tilawah_content_detail'
    template_name = 'Advance_Tilawah_detail.html'
