from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Tajweed2
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


class Tajweed2List(UserPassesTestMixin, ListView):
    model = Tajweed2
    context_object_name = 'tajweed2_content'
    template_name = 'Course2.html'

    def test_func(self):
        return self.request.user.username.startswith('tajweedlevel2')


class Tajweed2Detail(DetailView):
    model = Tajweed2
    context_object_name = 'tajweed2_content_detail'
    template_name = 'Course2detail.html'
