#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        
    def addToCart(self,customer,product,quantity):
        print("Added !")
        return True

customer_id = int(input("Enter Customer ID: "))
name = input("Enter customer name: ")
email = input("Enter customer email: ")
password=int(input("Enter customer password: "))
customer = customers(customer_id,name,email,password)

product_id = int(input("Enter Product ID: "))
name = input("Enter product name: ")
price =int(input("Enter product price: "))
description=input("Enter Product Description: ")
stock_quantity = int(input("Enter product stock quantity: "))
product = products(product_id,name,price,description,stock_quantity)

quantity=int(input("Enter quantity to add to the cart: "))
cart=cart(cart_id=4, customer_id=customer_id, product_id=product_id, quantity=quantity)

result=cart.addToCart(customer, product, quantity)

if result:
    print("Product added to the cart successfully.")
else:
    print("Failed to add the product to the cart.")


# In[ ]:




