from rest_framework import serializers
from .models import CustomerService, sales

class CustomerSerializer(serializers.ModelSerializer):
    customer_name=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'Customer name is required.'
            }
    )


    customer_type=serializers.ChoiceField(
            choices=CustomerService.customer_type.field.choices,
            required=True,
            error_messages={
                'required': 'Customer type is required.',
                'invalid_choice': 'Invalid customer type. Please choose a valid option.'
            }
        )

    contact_person=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'Contact person is required.'
            }
        )  

    email=serializers.EmailField(
            max_length=100,
            required=False,
            error_messages={
                'required': 'Email is required.',
                'invalid': 'Invalid email address. Please enter a valid email.'
            }
        )

    

    phone=serializers.IntegerField(
            max_length=10,
            required=False,
            unique=True,
            error_messages={
                'required': 'Contact number is required.',
                'invalid': 'Invalid contact number. Please enter a valid 10-digit number.'
            } 
    )

    address_Line_1=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'Address Line 1 is required.'
            }
    )

    city=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'City is required.'
            }
    )

    state=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'State is required.'
            }
    )

    gst_number=serializers.CharField(
            max_length=15,
            required=True,
            unique=True,
            startswith='GSTIN',
            error_messages={
                'required': 'GST number is required.'
            }
    )

    payment_terms=serializers.CharField(
            max_length=100,
            required=True,
            error_messages={
                'required': 'Payment terms is required.'
            }
    )

    status=serializers.BooleanField(
            required=True,
            error_messages={
                'required': 'Status is required.'
            }
    )
