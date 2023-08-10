
from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("content/<int:id>", views.content, name="content"),
    path("description/<int:id>", views.content_description, name="description")
    # re_path(r"^feature/([a-z-]+)(\d+)/$", views.feature,name="feature")
]