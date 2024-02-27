#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Products:
    def __init__(self, product_id=None, pname=None, price=None, description=None, stock_quantity=None):
        self.product_id = product_id
        self.pname = pname
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def get_product_id(self):
        return self.product_id

    def get_pname(self):
        return self.pname

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_stock_quantity(self):
        return self.stock_quantity

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_pname(self, pname):
        self.name = pname

    def set_price(self, price):
        self.price = price

    def set_description(self, description):
        self.description = description

    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity = stock_quantity    


# In[ ]:




