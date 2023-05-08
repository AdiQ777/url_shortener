from django.urls import path

from . import views

app_name = "shortener"

urlpatterns = [path("urls/", views.CreateShortURLAPIView.as_view(), name="shortened_url")]
