#!/usr/bin/env python
# coding: utf-8

# In[11]:


class customers:
    def __init__(self,customer_id,name,email,password):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.password=password
        
    def createCustomer(self):
        customer_id=int(input("Enter Customer ID:"))
        name=input("Enter Customer Name:")
        email=input("Enter Customer Email:")
        password=int(input("Enter Customer Password:"))

        new_customer = customers(customer_id=customer_id,name=name,email=email,password=password)
        
        print(f"Customer ID: {new_customer.customer_id}")
        print(f"Name: {new_customer.name}")
        print(f"Email: {new_customer.email}")
        print(f"Password:{new_customer.password}")
        return True
customers_instance=customers(customer_id=1,name="Yash",email="yash@example.com",password=1234)
result = customers_instance.createCustomer()
if result:
    print("Customer creation was successful.")
else:
    print("Customer creation failed.")
        


# In[ ]:




