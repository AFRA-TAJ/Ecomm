#!/usr/bin/env python
# coding: utf-8

# In[3]:


class products:
    def __init__(self,product_id,name,price,description,stock_quantity):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock_quantity=stock_quantity
        
    def get_product_id(self):
        return self.product_id
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_description(self):
        return self.description
    def get_stock_quantity(self):
        return self.stock_quantity
    
    def set_product_id(self):
        self.product_id=product_id
    def set_name(self):
        self.name=name
    def set_price(self):
        self.price=price
    def set_description(self):
        self.description=description
    def set_stock_quantity(self):
        self.stock_quantity=stock_quantity
        
    def print_info(self):
        print(f"Product  ID:{self.product_id}")
        print(f"Product Name:{self.name}")
        print(f"Price:{self.price}")
        print(f"Description:{self.description}")
        print(f"Stock Quantity:{self.stock_quantity}")
products_instance1=products(101,"mobile",15000,"long battery",200)
products_instance2=products(102,"tv",80000,"led screen",100)
products_instance3=products(103,"laptop",50000,"360 foldable",150)
products_instance1.print_info()
products_instance2.print_info()
products_instance3.print_info()    


# In[ ]:




