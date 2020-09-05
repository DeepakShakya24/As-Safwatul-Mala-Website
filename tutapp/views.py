from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from . import forms
from .models import AudioClip
from django.contrib.auth.models import User
from django.views.generic.detail import SingleObjectMixin
# Create your views here.


def index(request):
    return render(request, "index.html")


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AudioClipDetail(DetailView):
    model = AudioClip
    template_name = 'clips.html'
    context_object_name = "course_detail"


def homepage(request):
    return render(request, 'homepage.html')


class AudioClipList(ListView):
    model = AudioClip
    context_object_name = 'content'
    template_name = 'Course.html'


def About(request):
    return render(request, 'about.html')


def AboutUs(request):
    return render(request, 'aboutus.html')


def Whatistajweed(request):
    return render(request, 'what is tajweed.html')


def Importanceoftajweed(request):
    return render(request, 'importance of tajweed.html')


def Course2(request):
    return render(request, 'Course2.html')


def Course3(request):
    return render(request, 'Course3.html')
