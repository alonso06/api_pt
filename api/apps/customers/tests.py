from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import (CustomerType, Customer)

class CustomerTypeTests(APITestCase):
    def test_create_customer_type(self):
        """ Create customer type  """
        
        url = reverse('customertype-list')
        data = {'name': 'prueba'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(CustomerType.objects.count(), 1)
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)
        self.assertEqual(CustomerType.objects.get().name, 
                         'prueba')
        
    def test_no_create_customer_type(self):
        """ No create customer type, name > 12  """
        
        url = reverse('customertype-list')
        name = 'prueba con mas de 12 letras'
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        
        self.assertTrue(len(name)>12) 
        self.assertEqual(response.status_code, 
                         status.HTTP_400_BAD_REQUEST)
        


class CustomerTest(APITestCase):
    
    def test_create_customer(self):
        """ Create customer  """
        customer_type = CustomerType.objects.create(
            id=3, 
            name="Tipo Prueba")

        url = reverse('customer-list')
        data = {
            "first_name": "Prueba",
            "last_name": "Prueba",
            "sex": "M",
            "state": True,
            "birthdate": "1999-04-02",
            "customer_type_id": customer_type.id
        }
        
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)
         
    def test_no_create_customer(self):
        """ Unique values for sex: M,F | 
            first_name, last_name are required """
            
        customer_type = CustomerType.objects.create(
            id=3, 
            name="Tipo Prueba")
        value = 'A'
        url = reverse('customer-list')
        data = {
            "first_name": "Prueba",
            "last_name": "Prueba",
            "sex": value,
            "state": True,
            "birthdate": "1999-04-02",
            "customer_type_id": customer_type.id
        }
        
        response = self.client.post(url,data,format='json')
        self.assertNotEqual(value, 
                         ['M','F'])
        self.assertEqual(response.status_code, 
                         status.HTTP_400_BAD_REQUEST)