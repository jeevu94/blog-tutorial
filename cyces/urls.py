from django.contrib import admin
from django.urls import path
from .views import home, blogs

app_name = "cyces"

urlpatterns = [
    path("", home, name="home"),
    path("blogs", blogs, name="blogs"),
]
