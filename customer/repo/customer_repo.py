from ..models import Customer

class CustomerRepository:
    def get_customer_by_id(self, customer_id):
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None
