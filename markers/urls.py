from django.urls import path
from .views import Home, get_markers


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('get_markers/', get_markers, name='get_markers'),
]
