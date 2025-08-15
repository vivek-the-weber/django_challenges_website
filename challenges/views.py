from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "dec": "Decide your goals for next year"
     }

def index(request):
    list_of_months_response = list(months_challenges.keys())
    response = ""
    for month_redirect in list_of_months_response:
        reversed_path = reverse("month-challenge", args = [month_redirect]) # e.g. /challenge/jan
        response += f"<a href ='{reversed_path}'>{month_redirect}</a><br>"
    return HttpResponse(response)
def monthly_challenge_by_number(request, month):
    if month <= 12:
        months = list(months_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args = [redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("INVALID MONTH!!")
def monthly_challenge(request, month):
    try:
        challenges_text = months_challenges[month]
    except:
        return HttpResponseNotFound("Not a VALID FORMAT OF THE MONTH, enter jan, feb, etc...!!!")
    return HttpResponse(challenges_text)

