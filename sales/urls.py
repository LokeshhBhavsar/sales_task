from os import path
from django.urls import include, path,view

path('sales/create/', view.Createcustomer.as_view(), name='create_customer'),
path('sales/list/', view.Listcustomer.as_view(), name='list_customers'),
path('sales/detail/<str:customer_code>/', view.CustomerDetail.as_view(), name='customer_detail'),
path('sales/update/<str:customer_code>/', view.CustomerDetail.as_view(), name='update_customer'),
path('sales/delete/<str:customer_code>/', view.delete_customer.as_view(), name='delete_customer'),
path('sales/status/<str:customer_code>/', view.UpdateCustomerStatus.as_view(), name='update_status'),