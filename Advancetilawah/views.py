from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Advancetilawah
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


class AdvancetilawahList(UserPassesTestMixin, ListView):
    model = Advancetilawah
    context_object_name = 'tilawah_content'
    template_name = 'Advance Tilawah.html'

    def test_func(self):
        return self.request.user.username.startswith('AdvanceTilawah')


class AdvancetilawahDetail(DetailView):
    model = Advancetilawah
    context_object_name = 'tilawah_content_detail'
    template_name = 'Advance_Tilawah_detail.html'
