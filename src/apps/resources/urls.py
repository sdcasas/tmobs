from django.urls import path

from .views import get_redirect


urlpatterns = [
    path('get_redirect/<str:key>', get_redirect, name="get_redirect"),
]