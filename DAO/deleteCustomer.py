#!/usr/bin/env python
# coding: utf-8

# In[4]:


class customers:
    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password

    def deleteCustomer(self, customer_id_to_delete):
        if self.customer_id == customer_id_to_delete:
            print(f"Customer with ID {customer_id_to_delete} is deleted")
            return True
        else:
            raise CustomerNotFoundException(f"Customer with ID {customer_id_to_delete} not found")

class CustomerNotFoundException(Exception):
    pass

customer_instance = customers(customer_id=1, name="Yash", email="yash@example.com", password=1234)

try:
    result = customer_instance.deleteCustomer(1)
    print("Customer deletion was successful.")
except CustomerNotFoundException as e:
    print(f"Deletion failed: {e}")


# In[ ]:




