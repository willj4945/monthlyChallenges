from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for 20 minutes each day",
    "march": "Walk for 20 minutes each day",
    "april": "Walk for 20 minutes each day",
    "may": "Walk for 20 minutes each day",
    "june": "Walk for 20 minutes each day",
    "july": "Walk for 20 minutes each day",
    "august": "Walk for 20 minutes each day",
    "september": "Walk for 20 minutes each day",
    "october": "Walk for 20 minutes each day",
    "november": "Walk for 20 minutes each day",
    "december": "Walk for 20 minutes each day",
}


# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for i in months:
        month_path = reverse("month-challenge", args=[i])
        list_items += f"<li> <a href = \"{month_path}\">{i}</a></li>"

    response_data = f"{list_items}"
    return HttpResponse(response_data)


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month does not exist.")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("This month does not exist.")
