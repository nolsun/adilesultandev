from django.urls import path
from . import views

urlpatterns = [
    path('centercommentdata/', views.centercommentdata, name="centercommentdata")
]