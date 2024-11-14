from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.loan_eligibility_service import LoanEligibilityService
from utils.utils import standard_response

class LoanEligibilityCheck(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        loan_amount = request.data.get('loan_amount')
        interest_rate = request.data.get('interest_rate')
        tenure = request.data.get('tenure')

        # Validate input
        if not all([customer_id, loan_amount, interest_rate, tenure]):
            return standard_response(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Missing required fields in the request body."
            )

        loan_eligibility_service = LoanEligibilityService()
        response_data = loan_eligibility_service.check_eligibility(
            customer_id, loan_amount, interest_rate, tenure
        )

        if not response_data:
            return standard_response(
                status_code=status.HTTP_404_NOT_FOUND,
                message="Customer not found."
            )

        return standard_response(
            status_code=status.HTTP_200_OK,
            message="Loan eligibility checked.",
            data=response_data
        )
