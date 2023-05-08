from django.urls import path

from . import views

app_name = "shortener"

urlpatterns = [
    path("api/v1/urls/", views.CreateShortURLAPIView.as_view(), name="shortened_url"),
    path("<str:short_url>", views.ShortUrlRedirectView.as_view(), name="redirect"),
]
