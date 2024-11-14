# views.py
from rest_framework.views import APIView
from rest_framework import status
from .models import Customer
from .serializers import RegistrationSerializer, CustomerResponseSerializer
from utils.utils import standard_response
from django.db import IntegrityError



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import ingest_customer_data, ingest_loan_data

class CustomerDataIngestionView(APIView):
    def post(self, request):
        customer_file = request.FILES.get('customer_file')
        
        if not customer_file:
            return Response({"error": "Customer file is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        customer_file_path = f"media/{customer_file.name}"
        
        with open(customer_file_path, 'wb') as f:
            f.write(customer_file.read())
        
        # Trigger Celery task for ingesting customer data
        ingest_customer_data.delay(customer_file_path)
        
        return Response({"message": "Customer data ingestion is in progress."}, status=status.HTTP_200_OK)


class LoanDataIngestionView(APIView):
    def post(self, request):
        loan_file = request.FILES.get('loan_file')
        
        if not loan_file:
            return Response({"error": "Loan file is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        loan_file_path = f"media/{loan_file.name}"
        
        with open(loan_file_path, 'wb') as f:
            f.write(loan_file.read())
        
        # Trigger Celery task for ingesting loan data
        ingest_loan_data.delay(loan_file_path)
        
        return Response({"message": "Loan data ingestion is in progress."}, status=status.HTTP_200_OK)

class Registration(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            monthly_income = serializer.validated_data['monthly_income']
            approved_limit = round(36 * monthly_income, -5) 
            
            try:
                customer = Customer.objects.create(
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    age=serializer.validated_data['age'],
                    monthly_salary=monthly_income,
                    approved_limit=approved_limit,
                    phone_number=serializer.validated_data['phone_number']
                )

                response_serializer = CustomerResponseSerializer(customer)
                return standard_response(
                    status_code=status.HTTP_201_CREATED,
                    message="Customer registered successfully.",
                    data=response_serializer.data
                    )

            except IntegrityError:
                return standard_response(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    message="Customer could not be created due to an integrity error."
                )

        return standard_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Invalid data.",
            data=serializer.errors
        )
