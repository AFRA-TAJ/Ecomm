#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
class cart:
    def __init__(self,cart_id,customer_id,product_id,quantity):
        self.cart_id=cart_id
        self.customer_id=customer_id
        self.product_id=product_id
        self.quantity=quantity
        
    def getAllFromCart(self,customer):
        products_cart= [products(product_id=1,name="mobile",price=10000,description="long battery", stock_quantity=100),
                   products(product_id=2,name="tv",price=80000,description="led screen", stock_quantity=50),
                   products(product_id=3,name="laptop",price=50000,description="360 foldable", stock_quantity=150),
                   products(product_id=4,name="bluetooth",price=5000,description="wireless", stock_quantity=250)]
        return products_cart

cart =cart(cart_id=1, customer_id=customer_id, product_id=1, quantity=3)

products_cart=cart.getAllFromCart(customer)

for product in products_cart:
    print(f"Product ID:{product.product_id},Name:{product.name},Price:{product.price},Quantity:{product.stock_quantity}")


# In[ ]:




