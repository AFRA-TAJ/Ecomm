#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from EcommerceSystem import Order, Product, Quantity

class TestOrderPlacement(unittest.TestCase):

    def test_order_placement(self):
        customer = Customer("customer_id", "customer_name", "customer_email")
        product = Product("1", "product_name", 100)
        quantity = Quantity(2)
        product_list = [(product, quantity)]
        shipping_address = "customer_shipping_address"
        order = Order(customer, product_list, shipping_address)

        self.assertEqual(order.customer.customer_id, "customer_id")
        self.assertEqual(order.customer.name, "customer_name")
        self.assertEqual(order.customer.email, "customer_email")
        self.assertEqual(order.product_list[0][0].product_id, "1")
        self.assertEqual(order.product_list[0][0].name, "product_name")
        self.assertEqual(order.product_list[0][0].price, 100)
        self.assertEqual(order.product_list[0][1].quantity, 2)
        self.assertEqual(order.shipping_address, "customer_shipping_address")

