from django.urls import path
from myapp.views import home

# Create your views here.
urlpatterns = [
    path('',home)
]