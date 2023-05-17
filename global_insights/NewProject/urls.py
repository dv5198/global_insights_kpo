from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="global_insights"),
    path("aboutus/", views.about_us, name="about_us"),
    path("our_services/", views.service_1, name="services"),
    path("contact_us/", views.contact_, name="contact_us"),
]
urlpatterns += staticfiles_urlpatterns()