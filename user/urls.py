from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_user_by_pin/<str:pin>", views.get_user_by_pin, name="get_user_by_pin"),
]
