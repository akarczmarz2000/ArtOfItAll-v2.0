from django.urls import path
from . import views

urlpatterns = [
    path('', views.artrequest, name='art-request')
]