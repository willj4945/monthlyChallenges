from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'march':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'april':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'may':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'june':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'july':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'august':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'september':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'october':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'november':
        challenge_text = "Walk for 20 mins each day."
    elif month == 'december':
        challenge_text = "Walk for 20 mins each day."
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
