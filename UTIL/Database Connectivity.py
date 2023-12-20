#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[7]:


import mysql.connector as sql
conn=sql.connect(host='localhost',database='Ecomm',user='root',password='Af#ra_02!')#connecting with database
if conn.is_connected:
    print("Database is connected:")
    
stmt=conn.cursor()
create_str='''
create table if not exists customers
(
customer_id int,
name varchar(50),
email varchar(50),
password int
)
'''
stmt.execute(create_str)

stamt=conn.cursor()
creat_str='''
create table if not exists products
(
product_id int,
name varchar(50),
price int,
description varchar(100),
stock_quantity int
)
'''
stamt.execute(creat_str)

statmt=conn.cursor()
crete_str='''
create table if not exists cart
(
cart_id int,
customer_id int,
product_id int,
quantity int
)
'''
statmt.execute(crete_str)

stmet=conn.cursor()
cret_str='''
create table if not exists orders
(
order_id int,
customer_id int,
order_date date,
total_price int,
shippind_address varchar(100)
)
'''
stmet.execute(cret_str)

stment=conn.cursor()
ceate_str='''
create table if not exists order_items
(
order_items_id int,
order_id int,
product_id int,
quantity int
)
'''
stment.execute(ceate_str)

create_insert='''
insert into customers values(1,"yash","yash@example.com",1234),(2,"sen","sen@example.com",1342),(3,"kai","kai@example.com",3236)
'''
stmt=conn.cursor()
stmt.execute(create_insert)
conn.commit()
print('Inserted Successfully')

creat_insert='''
insert into products values(101,"mobile",15000,"long battery",200),(102,"tv",80000,"led screen",100),(103,"laptop",50000,"360 foldable",150)
'''
stamt=conn.cursor()
stamt.execute(creat_insert)
conn.commit()
print('Inserted Successfully')

creeate_insert='''
insert into cart values(11,1,101,200),(22,2,102,100),(33,3,103,150)
'''
statmt=conn.cursor()
statmt.execute(creeate_insert)
conn.commit()
print('Inserted Successfully')

ceate_insert='''
insert into orders values(201,1,"2023-12-02",70000,"123 st"),(202,2,"2023-10-07",50000,"241 st"),(203,3,"2023-04-21",80000,"153 st")
'''
stmet=conn.cursor()
stmet.execute(ceate_insert)
conn.commit()
print('Inserted Successfully')

createe_insert='''
insert into order_items values(44,201,101,200),(55,202,102,100),(66,203,103,150)
'''
stment=conn.cursor()
stment.execute(createe_insert)
conn.commit()
print('Inserted Successfully')


# In[ ]:




