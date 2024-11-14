from django.urls import path
from .api import LoanEligibilityCheck

urlpatterns = [
    path('check-eligibility/', LoanEligibilityCheck.as_view()),
]
