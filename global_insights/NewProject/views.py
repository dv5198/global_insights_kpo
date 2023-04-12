from django.shortcuts import render

# import calendly
# from calendlyapi import Client


# Create your views here.
def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about-us.html")


def contact_(request):
    return render(request, "contact_us.html")


def service_1(request):
    return render(request, "services.html")


def calendly_(request):
    return render(request, "calendly.html")


# def schedule_view(request):
#     client = Client(api_key="YOUR_API_KEY")
#     event_type = client.get_event_type("YOUR_EVENT_TYPE_ID")
#     event_link = event_type["url"]
#     return render(request, "schedule.html", {"event_link": event_link})
