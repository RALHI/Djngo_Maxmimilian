from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Eat no meat for entire month")

def february(request):
  return HttpResponse("Walk for at least 20 minutes every day")

