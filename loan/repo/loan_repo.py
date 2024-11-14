from ..models import Loan


class LoanRepository:
    def get_loan_history(self, customer_id):
        return Loan.objects.filter(customer_id=customer_id)
