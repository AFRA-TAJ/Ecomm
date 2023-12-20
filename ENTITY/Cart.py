#!/usr/bin/env python
# coding: utf-8

# In[4]:


class cart:
    def __init__(self,cart_id,customer_id,product_id,quantity):
        self.cart_id=cart_id
        self.customer_id=customer_id
        self.product_id=product_id
        self.quantity=quantity
        
    def get_cart_id(self):
        return cart_id
    def get_customer_id(self):
        return customer_id
    def get_product_id(self):
        return product_id
    def get_quantity(self):
        return quantity
    
    def set_cart_id(self):
        self.cart_id=cart_id
    def set_customer_id(self):
        self.customer_id=customer_id
    def set_product_id(self):
        self.product_id=product_id
    def set_quantity(self):
        self.quantity=quantity
        
    def print_info(self):
        print(f"Cart ID:{self.cart_id}")
        print(f"Customer ID:{self.customer_id}")
        print(f"Product ID:{self.product_id}")
        print(f"Quantity:{self.quantity}")
cart_instance1=cart(11,1,101,200)
cart_instance2=cart(22,2,102,100)
cart_instance3=cart(33,3,103,150)
cart_instance1.print_info()
cart_instance2.print_info()
cart_instance3.print_info()    
        


# In[ ]:


_

