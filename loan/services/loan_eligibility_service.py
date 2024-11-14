from ..repo.loan_repo import LoanRepository
from customer.repo.customer_repo import CustomerRepository
from .loan_service import LoanService
from django.db.models import Sum

class LoanEligibilityService:
    def __init__(self):
        self.loan_repository = LoanRepository()
        self.loan_service = LoanService()
        self.customer_repository = CustomerRepository()

    def check_eligibility(self, customer_id, loan_amount, interest_rate, tenure):
        customer = self.customer_repository.get_customer_by_id(customer_id)
        if not customer:
            return None 

        loan_history = self.loan_repository.get_loan_history(customer_id)

        credit_score = self.loan_service.calculate_credit_score(loan_history)

        approval, corrected_interest_rate = self.loan_service.get_loan_approval(
            credit_score, loan_amount, interest_rate, customer
        )

        if loan_history.aggregate(Sum('loan_amount'))['loan_amount__sum'] > customer.approved_limit:
            credit_score = 0
            approval = False

        monthly_installment = self.loan_service.calculate_monthly_installment(
            loan_amount, tenure, corrected_interest_rate
        )

        return {
            'customer_id': customer_id,
            'approval': approval,
            'interest_rate': interest_rate,
            'corrected_interest_rate': corrected_interest_rate,
            'tenure': tenure,
            'monthly_installment': monthly_installment
        }
