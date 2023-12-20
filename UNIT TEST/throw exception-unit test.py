#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from EcommerceSystem import Order, Product, Quantity

class TestOrderPlacementException(unittest.TestCase):

    def test_order_placement_exception(self):
        customer = Customer("customer_id", "customer_name", "customer_email")
        product = Product("1", "product_name", 100)
        quantity = Quantity(2)
        product_list = [(product, quantity)]
        shipping_address = "customer_shipping_address"
        order = Order(customer, product_list, shipping_address)

        with self.assertRaises(Exception) as context:
            order.placeOrder()

        self.assertTrue("Customer id or product id not found in database" in str(context.exception))

