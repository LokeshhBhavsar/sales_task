from sales.models import Customer
from django.db import transaction


class CustomerService:
    @staticmethod
    def _generate_customer_code():
        num = Customer.objects.count() + 1
        return "CUST-" + str(num)

    @staticmethod
    @transaction.atomic
    def create_customer(self,customer_name, customer_type, contact_person, email, phone_number, address_Line_1, adress_Line_2, city):
        customer = Customer(
            customer_code=self._generate_customer_code(),
            customer_name=customer_name,
            customer_type=customer_type,
            contact_person=contact_person,
            email=email,
            phone_number=phone_number,
            address_Line_1=address_Line_1,
            adress_Line_2=adress_Line_2,
            city=city
        )
        customer.save()
        return customer

    @staticmethod
    def get_customer_by_code(customer_code):
        try:
            return Customer.objects.get(customer_code=customer_code)
        except Customer.DoesNotExist:
            return "Customer not found"

    @staticmethod
    def update_customer(customer_code, **kwargs):
        customer = CustomerService.get_customer_by_code(customer_code)
        if not customer:
            return "Customer not found with this code"
        for key, value in kwargs.items():
            setattr(customer, key, value)
        customer.save()
        return customer

    @staticmethod
    def delete_customer(customer_code):
        customer = CustomerService.get_customer_by_code(customer_code)
        if not customer:
            return "Customer not found with this code"
        customer.delete()
        return "Customer deleted successfully"

    @staticmethod
    def list_customers():
        return Customer.objects.all()

    @staticmethod
    def update_status(customer_code, new_status):
        customer = CustomerService.get_customer_by_code(customer_code)
        if not customer:
            return "Customer not found with this code"
        customer.status = new_status
        customer.save()
        return customer