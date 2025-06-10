from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

month_challenges = {
  "january": "Eat no meat for entire month",
  "february": "Walk for at least 20 minutes every day",
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

# def index(request):
#   months = list(month_challenges.keys())
#   for month in months:
#     # capital_month = month.capitalize()
#     # month_path = reverse()
#     list_items += f"<li><a href="">{capital_month}</a></li>"
#   return HttpResponse(month)

def monthly_challenge_by_number(request,month):
  months = list(month_challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("<h1>Invalid Key</h1>")
  
  redirect_month = months[month-1]
  redirect_url = reverse("monthly_challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_url)

def monthly_challenge(request,month):
  try:
    challenges = month_challenges[month]
    response_html = f"<h1>{challenges}</h1>"
    return HttpResponse(response_html)
  except:
    return HttpResponseNotFound("<h1>Input month not supported</h1>")