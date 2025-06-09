from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

# def index(request):
#   return HttpResponse("Eat no meat for entire month")

# def february(request):
#   return HttpResponse("Walk for at least 20 minutes every day")

# def march(request):
#   return HttpResponse("Learn Django for at least 20 minutes daily")

def monthly_challenge(request,month):
  if month == "january":
    text = "Eat no meat for entire month"
  elif month == "february":
    text = "Walk for at least 20 minutes every day"
  elif month == "march":
    text = "Learn Django for at least 20 minutes daily"
  else:
    return HttpResponseNotFound("Input not supported")
  return HttpResponse(text)