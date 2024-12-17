from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact-inquiry", views.contactInquiry, name="contact-inquiry"),
]