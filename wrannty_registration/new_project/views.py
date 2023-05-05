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


# ----------------------WARRANTY FUNCTIONALITIES---------------------------------------
def warranty_register(request):
    if request.method == "POST":
        warranty_register = Warranty_Details.objects.create(
            user=request.user,
            product=request.POST["product"],
            brand_category=request.POST["brand_category"],
            model_number=request.POST["model_number"],
            serial_number=request.POST["serial_number"],
            date_of_purchase=request.POST["purchase_date"],
            place_of_purchase=request.POST["purchase_place"],
            proof_of_purchase=request.POST["purchase_proof"],
            date_of_delivery=request.POST["delivery_date"],
            warranty_valid_till=request.POST["warranty_valid"],
            # warranty_valid_till="2023-12-04",
            delivery_order=request.POST["delivery_order"],
            created_on=datetime.now(),
            updated_on=datetime.now(),
        )
        warranty_register.save()
        return redirect("success-page")

    return render(request, "warranty_registration.html")


# get warranty_details
def warranty_registration_detail(request):
    warranty_details = Warranty_Details.objects.all()
    context = {"warranty_details": warranty_details}
    return render(request, "warranty_details.html", context)


# ---------------------USER FUNCTIONALITIES -------------------------------------------


def User_Registration(request):
    if request.method == "POST":
        full_name = request.POST["f_name"] + " " + request.POST["l_name"]
        if User_Details.objects.filter(email=request.POST["email"]).exists():
            messages.success(request, "Email Already exists")
            return redirect("user_register")
        user = User_Details.objects.create_user(
            username=request.POST["email"],
            title=request.POST["title"],
            name=full_name,
            email=request.POST["email"],
            password=request.POST["user_password"],
            phone_no=request.POST["phno_"],
            created_on=datetime.now(),
            updated_on=datetime.now(),
            is_staff=False,
        )
        user.save()
        messages.success(request, "Registered Successfully")
        return redirect("user_login")
    else:
        messages.success(request, "Something Went Wrong ")
        return render(request, "register.html")


# ------------USER LOGIN -------------


def User_Login(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        phone_number = 9265768306
        password = request.POST["user_password"]
        user = User_Details.objects.filter(phone_no=phone_number).first()

        if not user or not user.check_password(password):
            messages.error(request, "Invalid phone number or password.")
            return redirect("user_login")

        # Send OTP to user's phone number
        otp = generate_otp()
        send_otp(phone_number, otp)

        # Show OTP verification form to user
        return render(
            request, "otp_verification.html", {"phone_number": phone_number, "otp": otp}
        )

    return render(request, "login.html")


# @csrf_exempt
def send_otp(request):
    phone_number = request.POST.get("phone_number")
    pass


# ------------OTP VERIFICATION -------------
def verify_otp(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        otp = request.POST.get("otp")

        # Verify the OTP entered by the user with the OTP sent to their phone number
        if otp == User_Details.objects.filter(phone_no=phone_number).first().otp:
            # OTP is verified, allow the user to log in
            # Set session variable or cookie to indicate that the user is logged in
            # Redirect the user to the dashboard or home page
            return redirect("dashboard")
        else:
            # OTP is not verified, show an error message
            messages.error(request, "Invalid OTP.")
            return redirect("user_login")

    return render(request, "otp_verification.html")


# ------------USER LOGOUT  -------------

# @login_required
# def UserLogout(request):
# logout(request)
# return redirect("ecommerce_site")
