from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views import generic

# Create your views here.
class SignUp(CreateView, generic.RedirectView):
    None
