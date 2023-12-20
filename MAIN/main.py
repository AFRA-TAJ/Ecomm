#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ENTITY.customers import customers
from ENTITY.products import products
from ENTITY.orders import orders
from ENTITY.cart import cart
from ENTITY.order_items import order_items
from DAO.createProduct import createProduct
from DAO.createCustomer import createCustomer
from DAO.deleteProduct import deleteProduct
from DAO.deleteCustomer import deleteCustomer
from DAO.addToCart import addToCart
from DAO.removeFromCart import removeFromCart
from DAO.getAllFromCart import getAllFromCart
from DAO.getOrderByCustomer import getOrderByCustomer
from EXCEPTION.CustomerNotFoundException import CustomerNotFoundException
from EXCEPTION.ProductNotFoundException import ProductNotFoundException
from EXCEPTION.OrderNotFoundException import OrderNotFoundException
import unittest

class EcomService:
    def __init__(self):
        self.createcustomer=createCustomer()
        self.createproduct=createProduct()
        self.deleteproduct=deleteProduct()
        self.addtocart=addToCart()
        self.getallfromcart=getAllFromCart()
        self.getorderbycustomer=getOrderByCustomer()

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
    
    def createProduct(self):
        product_id=int(input("Enter Product ID:"))
        name=input("Enter product name: ")
        price=int(input("Enter product price: "))
        description=input("Enter prodcut description:")
        stock_quantity=int(input("Enter product quantity: "))

        new_product=products(product_id=product_id,name=name,price=price,description=description,stock_quantity=stock_quantity)

        print(f"Product ID:{new_product.product_id}")
        print(f"Name: {new_product.name}")
        print(f"Price: ${new_product.price}")
        print(f"Description:{new_product.description}")
        print(f"Stock Quantity: {new_product.stock_quantity}")
        return True

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


    def addToCart(self,customer,product,quantity):
        print("Added !")
        return True
    
    def getAllFromCart(self,customer):
        products_cart= [products(product_id=1,name="mobile",price=10000,description="long battery", stock_quantity=100),
                   products(product_id=2,name="tv",price=80000,description="led screen", stock_quantity=50),
                   products(product_id=3,name="laptop",price=50000,description="360 foldable", stock_quantity=150),
                   products(product_id=4,name="bluetooth",price=5000,description="wireless", stock_quantity=250)]
        return products_cart
            
    def getOrdersByCustomer(customerid):
        orders ={1:{"product":"mobile","quantity":100},2: {"product":"tv","quantity":50}, 3: {"product":"laptop","quantity":70},
                  4: {"product":"bluetooth","quantity":150}}

        customer_orders = [{"product": order["product"], "quantity": order["quantity"]}
        for order_id, order in orders.items()
        if order.get("customerid")==customerid]

        return customer_orders 

class EcomApp:
    def __init__(self):
        self.ecom_service = EcomService()

    def display_menu(self):
        print("E-commerce Application Menu:")
        print("1. Create Customer")
        print("2. Create Product")
        print("3. Delete Product")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. View Customer Order")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.ecom_service.createCustomer()
            elif choice == "2":
                self.ecom_service.createProduct()
            elif choice == "3":
                self.ecom_service.deleteProduct()
            elif choice == "4":
                self.ecom_service.add_to_cart()
            elif choice == "5":
                self.ecom_service.view_cart()
            elif choice == "6":
                self.ecom_service.view_customer_order()
            elif choice == "7":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    ecom_app = EcomApp()
    ecom_app.run()


# In[ ]:




