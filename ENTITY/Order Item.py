#!/usr/bin/env python
# coding: utf-8

# In[1]:


class order_items:
    def __init__(self,order_item_id,order_id,product_id,quantity):
        self.order_item_id=order_item_id
        self.order_id=order_id
        self.product_id=product_id
        self.quantity=quantity
        
    def get_order_item_id(self):
        return order_item_id
    def get_order_id(self):
        return order_id
    def get_product_id(self):
        return product_id
    def get_quantity(self):
        return quantity
    
    def set_order_item_id(self):
        self.order_item_id=order_item_id
    def set_order_id(self):
        self.order_id=orderr_id
    def set_product_id(self):
        self.product_id=product_id
    def set_quantity(self):
        self.quantity=quantity
        
    def print_info(self):
        print(f"Order Item ID:{self.order_item_id}")
        print(f"Order ID:{self.order_id}")
        print(f"Product ID:{self.product_id}")
        print(f"Quantity:{self.quantity}")
order_items_instance1=order_items(44,201,101,200)
order_items_instance2=order_items(55,202,102,100)
order_items_instance3=order_items(66,203,103,150)
order_items_instance1.print_info()
order_items_instance2.print_info()
order_items_instance3.print_info() 


# In[ ]:




