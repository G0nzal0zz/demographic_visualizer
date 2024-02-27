from django.shortcuts import render, HttpResponse

def home(request, city):
    return HttpResponse("Esta ciudad esta troll " + city)