#!/usr/bin/env python
# coding: utf-8

# In[2]:


class customers:
    def __init__(self,customer_id,name,email,password):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.password=password
        
    def get_customer_id(self):
        return self.customer_id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    
    def set_customer_id(self):
        self.customer_id=customer_id
    def set_name(self):
        self.name=name
    def set_email(self):
        self.email=email
    def set_password(self):
        self.password=password
        
    def print_info(self):
        print(f"Customer ID:{self.customer_id}")
        print(f"Customer Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Password:{self.password}")
customers_instance1=customers(1,"yash","yash@example.com",1234)
customers_instance2=customers(2,"sen","sen@example.com",1342)
customers_instance3=customers(3,"kai","kai@example.com",3236)
customers_instance1.print_info()
customers_instance2.print_info()
customers_instance3.print_info()    


# In[ ]:




