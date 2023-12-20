#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class CustomerNotFoundException(Exception):
    def __init__(self, message="Invalid Customer ID"):
        self.message = message
        super().__init__(self.message)
        
class ProductNotFoundException(Exception):
    def __init__(self, message="Invalid Product ID"):
        self.message = message
        super().__init__(self.message)

class OrderNotFoundException(Exception):
    def __init__(self, message="Invalid Order ID"):
        self.message = message
        super().__init__(self.message)

