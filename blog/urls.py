from django.urls import path
from blog.views import home

# Create your views here.
urlpatterns = [
    path('',home)
]