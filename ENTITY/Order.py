#!/usr/bin/env python
# coding: utf-8

# In[4]:


class orders:
    def __init__(self,order_id,customer_id,order_date,total_price,shipping_address):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_date=order_date
        self.total_price=total_price
        self.shipping_address=shipping_address
        
    def get_order_id(self):
        return order_id
    def get_customer_id(self):
        return customer_id
    def get_order_date(self):
        return order_date
    def get_total_price(self):
        return total_price
    def get_shipping_address(self):
        return shipping_address
    
    def set_order_id(self):
        self.order_id=order_id
    def set_customer_id(self):
        self.customer_id=customer_id
    def set_order_date(self):
        self.order_date=order_date
    def set_total_price(self):
        self.total_price=total_price
    def set_shipping_address(self):
        self.shipping_address=shipping_address
        
    def print_info(self):
        print(f"Order ID:{self.order_id}")
        print(f"Customer ID:{self.customer_id}")
        print(f"Order Date:{self.order_date}")
        print(f"Total Price:{self.total_price}")
        print(f"Shipping Address:{self.shipping_address}")
orders_instance1=orders(201,1,"2023-12-02",70000,"123 st")
orders_instance2=orders(202,2,"2023-10-07",50000,"241 st")
orders_instance3=orders(203,3,"2023-04-21",80000,"153 st")
orders_instance1.print_info()
orders_instance2.print_info()
orders_instance3.print_info() 


# In[ ]:




