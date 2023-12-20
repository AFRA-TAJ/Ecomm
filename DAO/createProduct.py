#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Products:
    def __init__(self,product_id,name,price,description,stock_quantity):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock_quantity=stock_quantity

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
product_instance = Products(product_id=1,name="mobile",price=20000,description="long battery",stock_quantity=50)
result=product_instance.createProduct()
if result:
    print("Product created successfully.")
else:
    print("Product creation failed.")


# In[ ]:




