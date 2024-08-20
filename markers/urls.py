from django.urls import path
from markers import views


urlpatterns = [
    path("", views.Home.as_view()),
]
