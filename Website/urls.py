from django.urls import path
from Website.views import index, about, contact

urlpatterns = [
    path("", index),
    path("about", about),
    path("contact", contact),
]
