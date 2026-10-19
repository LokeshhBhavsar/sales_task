from django.http import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializer import CustomerSerializer


class Createcustomer(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if not request.data:
            return Response({"error": "Request body is empty"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Customer created successfully"}, status=status.HTTP_201_CREATED)

        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    


class Listcustomer(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if not request.data:
            return Response({"error": "Request body is empty"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Customer list retrieved successfully"}, status=status.HTTP_200_OK)

        
    


class CustomerDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, customer_code):
        if not request.data:
            return Response({"error": "Request body is empty"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": f"Customer details for {customer_code} retrieved successfully"}, status=status.HTTP_200_OK)

class UpdateCustomerStatus(APIView):
    permission_classes = [AllowAny]

    def put(self, request, customer_code):
        return Response({"message": f"Customer status for {customer_code} updated successfully"}, status=status.HTTP_200_OK)

class delete_customer(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, customer_code):
        return Response({"message": f"Customer {customer_code} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class update_status(APIView):
    permission_classes = [AllowAny]

    def put(self, request, customer_code):
        return Response({"message": f"Customer status for {customer_code} updated successfully"}, status=status.HTTP_200_OK)

    