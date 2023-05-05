from . import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("about_us", views.about_, name="about_us"),
    path("contact_us", views.contact_, name="contact_us"),
    path("user_login", views.login_, name="user_login"),
    path("user_signup/", views.User_Login, name="user_signup"),
    path("user_register", views.register_, name="user_register"),
    path("user_registration/", views.User_Registration, name="user_registration"),
    path("warranty/", views.warranty_, name="warrant_register"),
    path(
        "warranty_registration/",
        views.warranty_registration_detail,
        name="warranty_registration",
    ),
    # path("send_otp/", views.send_otp, name="send_otp"),
]
