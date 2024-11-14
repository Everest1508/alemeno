from django.db.models import Sum
from datetime import date

class LoanService:
    def calculate_credit_score(self, loan_history):

        paid_on_time = loan_history.aggregate(Sum('emis_paid_on_time'))['emis_paid_on_time__sum'] or 0
        number_of_loans = loan_history.count()
        loan_activity = loan_history.filter(end_date__gte=date.today()).count()  # Active loans
        approved_volume = loan_history.aggregate(Sum('loan_amount'))['loan_amount__sum'] or 0

        print(paid_on_time,number_of_loans,loan_activity,approved_volume)

        credit_score = (
            0.4 * paid_on_time +
            0.2 * number_of_loans +
            0.1 * loan_activity +
            0.3 * float(approved_volume)
        )

        print(credit_score)

        return credit_score

    def get_loan_approval(self, credit_score, loan_amount, interest_rate, customer):
        print(credit_score,loan_amount,interest_rate)
        approval = False
        corrected_interest_rate = interest_rate

        if credit_score > 50:
            approval = True
        elif 30 < credit_score <= 50:
            if interest_rate <= 12:
                corrected_interest_rate = 12
                approval = True
        elif 10 < credit_score <= 30:
            if interest_rate <= 16:
                corrected_interest_rate = 16
                approval = True
        elif credit_score <= 10:
            approval = False

        if customer.approved_limit > 0.5 * float(customer.monthly_salary):
            approval = False

        return approval, corrected_interest_rate

    def calculate_monthly_installment(self, loan_amount, tenure, interest_rate):
        monthly_interest_rate = interest_rate / 100 / 12
        emi = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-tenure))
        return round(emi, 2)
