from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

month_challenges = {
  "january": "Eat no meat for entire month",
  "feruary": "Walk for at least 20 minutes every day",
  "march": "Learn Django for at least 20 minutes daily",
  "april": "Eat no meat for entire month",
  "may": "Walk for at least 20 minutes every day",
  "june": "Learn Django for at least 20 minutes daily",
  "july": "Eat no meat for entire month",
  "august": "Walk for at least 20 minutes every day",
  "september": "Learn Django for at least 20 minutes daily",
  "october": "Eat no meat for entire month",
  "november": "Walk for at least 20 minutes every day",
  "december": "Learn Django for at least 20 minutes daily",
}

def monthly_challenge(request,month):
  try:
    challenges = month_challenges[month]
    return HttpResponse(challenges)
  except:
    return HttpResponseNotFound("Input month not supported")