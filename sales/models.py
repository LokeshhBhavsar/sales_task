from django.db import models
from django.conf import settings


class CustomerService(models.Model):

    customer_code = models.CharField(
        primary_key=True,
        max_length=100,
        unique=True
    )


    customer_name = models.CharField(
        max_length=100
    )

    customer_type = models.CharField(
        # Company = 'Company',
        # Individual = 'Individual',
        # Distributor = 'Distributor',
        # Dealer = 'Dealer',
        # Contractor = 'Contractor',
        # other = 'other',

        choices=[
             'Company',
             'Individual',
             'Distributor',
             'Dealer',
             'Contractor',
             'other',
        ],

    )

    contact_person = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        max_length=100,
        unique=True
    )

    phone= models.CharField(
        max_length=10,
        unique=True
    )

    address = models.TextField(
        max_length=100  
    )

    city = models.CharField(
        max_length=100
    )


    state = models.CharField(
        max_length=100
    )

    gst_number = models.CharField(
        max_length=15,
        unique=True
    )

    payment_terms = models.CharField(
        # immediate = 'Immediate',
        # net_15 = 'Net 15',
        # net_30 = 'Net 30',
        # net_45 = 'Net 45',
        # net_60 = 'Net 60',
        # net_90 = 'Net 90',

        choices=['immediate', 'net_15', 'net_30', 'net_45', 'net_60', 'net_90']
        ,

    )

    status=models.CharField(
        # active = 'Active',
        # inactive = 'Inactive',
        default='Active',
        choices=['Active', 'Inactive']
    )

    class Meta:
        db_table = 'Customer_Details'


