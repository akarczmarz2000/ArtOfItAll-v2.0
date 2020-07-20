from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('<artist_id>', views.artist_details, name='artist_details'),
]