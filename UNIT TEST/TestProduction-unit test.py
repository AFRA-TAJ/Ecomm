#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from EcommerceSystem import Product

class TestProductCreation(unittest.TestCase):

    def test_product_creation(self):
        product = Product("1", "product_name", 100)
        self.assertEqual(product.product_id, "1")
        self.assertEqual(product.name, "product_name")
        self.assertEqual(product.price, 100)

if __name__ == '__main__':
    unittest.main()

