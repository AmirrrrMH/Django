from django.urls import path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path("", index, name="home"),
    path("single", single_blog, name="single"),
]
