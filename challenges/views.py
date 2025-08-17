from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.

months_challenges = {
    "jan": "Do Pushups", 
    "feb" : "Workout", 
    "mar" : "Wash your hands", 
    "apr" : "Wish yourself luck",
    "may" : "Stay at home", 
    "jun" : "Do some fun",
    "jul" : "Don't you lie",
    "aug":"Pick up the log",
    "sep" : "Step on november", 
    "oct":"opt for volunteering",
    "nov" : "Go to the Chember",
    "dec": None,
     }

def index(request):
    list_of_months_response = list(months_challenges.keys())
    return render(request,"challenges/index.html", {
        "months" : list_of_months_response,
    })
def monthly_challenge_by_number(request, month):
    if month <= 12:
        months = list(months_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args = [redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404()
def monthly_challenge(request, month):

    try:
        challenge_text = months_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text, "month_name" : month,
        })
    except:
        raise Http404()