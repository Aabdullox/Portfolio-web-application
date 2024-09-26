from django.urls import path
from work.views import home

urlpatterns = [
    path('', home, name="home"),
]