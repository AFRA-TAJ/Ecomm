#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from EcommerceSystem import Product, Quantity

class TestAddProductToCart(unittest.TestCase):

    def test_add_product_to_cart(self):
        product = Product("1", "product_name", 100)
        quantity = Quantity(2)
        product_list = [(product, quantity)]

        self.assertEqual(len(product_list), 1)
        self.assertEqual(product_list[0][0].product_id, "1")
        self.assertEqual(product_list[0][0].name, "product_name")
        self.assertEqual(product_list[0][0].price, 100)
        self.assertEqual(product_list[0][1].quantity, 2)

