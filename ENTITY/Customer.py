#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Customers:
    def __init__(self, customer_id=None, cname=None, email=None, password=None):
        self.customer_id = customer_id
        self.cname = cname
        self.email = email
        self.password = password

    def get_customer_id(self):
        return self.customer_id

    def get_cname(self):
        return self.cname

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_cname(self, cname):
        self.cname = cname

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password   


# In[ ]:




