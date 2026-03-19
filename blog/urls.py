from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_home, name='home'),
    path('<int:pid>', views.blog_single, name='single'),
    path('category/<str:cat_name>', views.blog_home, name='category'),
    path("author/<str:author_username>", views.blog_home, name="author"),
    path("search/", views.search, name="search"),
    path('test/', views.test),
]
