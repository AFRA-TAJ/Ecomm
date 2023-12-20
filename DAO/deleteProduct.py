#!/usr/bin/env python
# coding: utf-8

# In[4]:


class products:
    def __init__(self,product_id,name,price,description,stock_quantity):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock_quantity=stock_quantity
        
    def deleteProduct(self,product_id):
        product_id=int(input("Enter Product ID to delete:"))
        print(f"Product with {product_id} is deleted")
        return True
product_instance = products(product_id=1,name="mobile",price=20000,description="long battery",stock_quantity=50)
result=product_instance.deleteProduct(4)
if result:
    print("Product deletion was successful.")
else:
    print("Product deletion failed.")


# In[ ]:




