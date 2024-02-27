#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from ENTITY.Customer import Customers
from ENTITY.Product import Products
from DAO.OrderProcess import OrderProcessorRepository

class TestEcommerce(unittest.TestCase):
    def setUp(self):
        # Create an instance of OrderProcessorRepository before each test
        self.opr = OrderProcessorRepository()

    def test_product_creation(self):
        prod = Products(product_id=102, pname='TV', price=80000, description='LED screen.', stock_quantity=200)
        result = self.opr.create_product(product=prod)
        self.assertTrue(result, 'Product Creation Successful.')

    def test_customer_registration(self):
        cust = Customers(customer_id=1, cname='yash', email='yash@example.com', password='1234')
        result = self.opr.create_customer(customer=cust)
        self.assertTrue(result, 'Customer Registration Successful.')

if __name__ == '__main__':
    unittest.main()
