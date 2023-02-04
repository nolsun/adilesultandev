from django.urls import path
from . import views

urlpatterns = [
    path('branchmonthlydata/', views.branchmonthlydata, name="branchmonthlydata")
]