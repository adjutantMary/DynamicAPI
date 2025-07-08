from django.urls import path
from .views import CalculateBonusView

urlpatterns = [
    path("calculate-bonus/", CalculateBonusView.as_view(), name="calculate-bonus")
]