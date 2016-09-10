from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect



def display_home_page(request):
    return render(request, "home/home_page.html")