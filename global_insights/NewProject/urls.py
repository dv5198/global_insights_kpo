from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='global_insights'),
    path('aboutus',views.about_us,name='about_us'),
    path('our_services',views.service_1,name='services'),
    path('services',views.service_2,name='services2'),
    path('contact_us',views.about_us,name='contact_us'),
]