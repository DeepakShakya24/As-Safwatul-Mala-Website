from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tutapp.models import Jazariyyah
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.


class JazariyyahList(UserPassesTestMixin, ListView):
    model = Jazariyyah
    context_object_name = 'jazariyyah_content'
    template_name = 'jazariyyah.html'

    def test_func(self):
        return self.request.user.username.startswith('Jazariyyah')


class JazariyyahDetail(DetailView):
    model = Jazariyyah
    context_object_name = 'jazariyyah_content_detail'
    template_name = 'jazariyyah_detail.html'
