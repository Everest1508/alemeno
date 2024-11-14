from celery import shared_task
from celery import chain  # Import chain to create a chain of tasks
import pandas as pd
from .models import Customer
from loan.models import Loan
from datetime import datetime

@shared_task
def ingest_customer_data(file_path):
    # Load the customer data from the Excel file
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    
    # Clean column names by stripping spaces
    df.columns = df.columns.str.strip()
    
    # Iterate over the rows to insert/update customer records
    for _, row in df.iterrows():
        print(row)  # For debugging, you can remove this later
        
        # Extract customer data from the row
        customer_id = row['Customer ID']
        first_name = row['First Name']
        last_name = row['Last Name']
        phone_number = row['Phone Number']
        monthly_salary = row['Monthly Salary']
        approved_limit = row['Approved Limit']
        age = row['Age']
        
        # Insert or update the customer record
        customer, created = Customer.objects.update_or_create(
            id=customer_id,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'monthly_salary': monthly_salary,
                'approved_limit': approved_limit,
                'age': age,
            }
        )
    
    return "Customer data ingestion completed."


@shared_task
def ingest_loan_data(file_path):
    # Load the loan data from the Excel file
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    
    # Clean column names by stripping spaces
    df.columns = df.columns.str.strip()
    
    # Iterate over the rows to insert/update loan records
    for _, row in df.iterrows():
        print(row)  # For debugging, you can remove this later
        
        # Extract loan data from the row
        customer_id = row['Customer ID']
        loan_id = row['Loan ID']
        loan_amount = row['Loan Amount']
        tenure = row['Tenure']
        interest_rate = row['Interest Rate']
        monthly_repayment = row['Monthly payment']
        emis_paid_on_time = row['EMIs paid on Time']
        start_date = row['Date of Approval']
        end_date = row['End Date']
        
        # Retrieve the customer object
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            print(f"Customer with ID {customer_id} does not exist.")
            continue  # Skip the loan if the customer does not exist
        
        # Insert or update the loan record
        loan, created = Loan.objects.update_or_create(
            loan_id=loan_id,
            customer=customer,
            defaults={
                'loan_amount': loan_amount,
                'tenure': tenure,
                'interest_rate': interest_rate,
                'monthly_repayment': monthly_repayment,
                'emis_paid_on_time': emis_paid_on_time,
                'start_date': start_date,
                'end_date': end_date,
            }
        )
    
    return "Loan data ingestion completed."
