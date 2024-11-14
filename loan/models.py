from django.db import models

# Create your models here.
class Loan(models.Model):
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE, db_column='customer_id')
    loan_id = models.IntegerField(null=True)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure = models.IntegerField() 
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  
    monthly_repayment = models.DecimalField(max_digits=10, decimal_places=2)  
    emis_paid_on_time = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
