from datetime import datetime
import os
import random
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from new_project.models import User_Details, Warranty_Details
from django.contrib import messages
from django.contrib.auth import login, logout
import requests
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def about_(request):
    return render(request, "about.html")


def contact_(request):
    return render(request, "contact.html")


def login_(request):
    return render(request, "login.html")


def register_(request):
    return render(request, "register.html")


def warranty_(request):
    return render(request, "warranty_registration.html")
