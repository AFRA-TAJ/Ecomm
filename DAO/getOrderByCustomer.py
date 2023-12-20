#!/usr/bin/env python
# coding: utf-8

# In[10]:


class customers:
    def __init__(self,customer_id,name,email,password):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.password=password
class products:
    def __init__(self,product_id,name,price,description,stock_quantity):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock_quantity=stock_quantity
class orders:
    def __init__(self,order_id,customer_id,order_date,total_price,shipping_address):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_date=order_date
        self.total_price=total_price
        self.shipping_address=shipping_address
class order_items:
    def __init__(self,order_item_id,order_id,product_id,quantity):
        self.order_item_id=order_item_id
        self.order_id=order_id
        self.product_id=product_id
        self.quantity=quantity
        
def getOrdersByCustomer(customerid):
        orders ={1:{"product":"mobile","quantity":100},2: {"product":"tv","quantity":50}, 3: {"product":"laptop","quantity":70},
                  4: {"product":"bluetooth","quantity":150}}

        customer_orders = [{"product": order["product"], "quantity": order["quantity"]}
        for order_id, order in orders.items()
        if order.get("customerid")==customerid]

        return customer_orders
customer_id_to_search = 1
orders = getOrdersByCustomer(customer_id_to_search)
print(orders)


# In[ ]:




