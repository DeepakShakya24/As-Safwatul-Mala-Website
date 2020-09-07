from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Tajweed3
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


class Tajweed3List(UserPassesTestMixin, ListView):
    model = Tajweed3
    context_object_name = 'tajweed3_content'
    template_name = 'Course3.html'

    def test_func(self):
        return self.request.user.username.startswith('tajweedlevel3')


class Tajweed3Detail(DetailView):
    model = Tajweed3
    context_object_name = 'tajweed3_content_detail'
    template_name = 'Course3detail.html'
