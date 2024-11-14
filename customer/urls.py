from django.urls import path
from .api import Registration,LoanDataIngestionView,CustomerDataIngestionView

urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
    path('loan-ingest/',LoanDataIngestionView.as_view()),
    path('customer-ingest/',CustomerDataIngestionView.as_view()),
]
