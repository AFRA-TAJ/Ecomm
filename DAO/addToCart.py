#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as sql
from UTIL.DBConnUtil import DbConnect
from EXCEPTION.Exceptions import ProductNotFoundException, CustomerNotFoundException, OrderNotFoundException

class OrderProcessorRepository(DbConnect):
    def __init__(self):
        self.db_connection = DbConnect()

    def create_product(self, product):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''INSERT INTO products (product_id, pname, price, description, stock_quantity)
                    VALUES ('{product.product_id}', '{product.pname}', '{product.price}', '{product.description}', '{product.stock_quantity}')'''
            )
            print(f"Product with {product.product_id} created successfully.")
            self.db_connection.conn.commit()
            return True
        except Exception as e:
            print(e)
            raise ProductNotFoundException("Failed to create product.")
        finally:
            self.db_connection.close()

    def delete_product(self, product_id):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(f'''Delete From products Where product_id = {product_id}''')
            print(f'\nDeleted Product with ID - {product_id} from the database.')
            self.db_connection.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.db_connection.close()

    def create_customer(self, customer):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''INSERT INTO customers (customer_id, cname, email, password)
                    VALUES ('{customer.customer_id}', '{customer.cname}', '{customer.email}', '{customer.password}')'''
            )
            print(f"Customer with {customer.customer_id} created successfully")
            self.db_connection.conn.commit()
            return True

        except Exception as e:
            print(e)
            raise CustomerNotFoundException("Failed to create customer.")

        finally:
            self.db_connection.close()

    def delete_customer(self, customer_id):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(f'''DELETE FROM customers WHERE customer_id = {customer_id}''')
            print("Customer deleted successfully.")
            self.db_connection.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.db_connection.close()

    def add_to_cart(self, cart, product, quantity):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''INSERT INTO cart (cart_id, customer_id, product_id, quantity)
                       VALUES ({cart.cart_id}, {cart.customer_id}, {product.product_id}, {quantity})'''
            )
            print(f'\nItems added to the cart.')
            self.db_connection.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.db_connection.close()

    def remove_from_cart(self, customer, product):
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''DELETE FROM cart WHERE customer_id = {customer.customer_id} 
                AND product_id = {product.product_id}'''
            )
            self.db_connection.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db_connection.close()

    def get_all_from_cart(self, customer_id):
        products_in_cart = []
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''SELECT product_id, quantity
                    FROM cart
                    WHERE customer_id = {customer_id}'''
            )
            for row in self.db_connection.stmt:
                product_id, quantity = row[0], row[1]
                products_in_cart.append({'product_id': product_id, 'quantity': quantity})
        except Exception as e:
            print(e)
        finally:
            self.db_connection.close()
            return products_in_cart

    def place_order(self, customer_id, order_id, order_items):
        total_price = 0

        try:
            for product_id, quantity, order_item_id in order_items:
                self.db_connection.open()
                self.db_connection.stmt.execute(
                    f'SELECT price FROM products WHERE product_id = %s', (product_id,)
                )
                rows = self.db_connection.stmt.fetchall()

                if rows:
                    cost = rows[0][0]
                    total_price += quantity * float(cost)
                self.db_connection.close()
        except Exception as e:
            print(e)
            return False

        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''INSERT INTO orders (order_id, customer_id, order_date, total_price)
                    VALUES (%s, %s, CURRENT_DATE(), %s)''',
                (order_id, customer_id, total_price)
            )
            self.db_connection.conn.commit()
        except Exception as e:
            print(e)
            return False

        try:
            for product_id, quantity, order_item_id in order_items:
                self.db_connection.open()
                self.db_connection.stmt.execute(
                    f'''INSERT INTO order_items (order_item_id, order_id, product_id, quantity)
                        VALUES (%s, %s, %s, %s)''',
                    (order_item_id, order_id, product_id, quantity)
                )
                self.db_connection.conn.commit()

                # Updating stock quantity
                self.db_connection.stmt.execute(
                    f'''UPDATE products SET stockQuantity = stockQuantity - %s
                        WHERE product_id = %s''',
                    (quantity, product_id)
                )
                self.db_connection.conn.commit()
                self.db_connection.close()
        except Exception as e:
            print(e)
            return False

        print(f'\nOrder Placed Successfully..\nYour Order ID is {order_id}.')
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(
                f'''DELETE FROM cart WHERE customer_id = %s''', (customer_id,)
            )
            self.db_connection.conn.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            self.db_connection.close()

        return True

    def get_orders_by_customer(self, customer_id):
        orders = []
        try:
            self.db_connection.open()
            self.db_connection.stmt.execute(f'''SELECT *
                                 FROM orders
                                 WHERE customer_id = {customer_id}''')

            orders = self.db_connection.stmt.fetchall()

            print('\nThese are the Orders placed:')
            for order in orders:
                print(order)

        except Exception as e:
            print(e)
        finally:
            self.db_connection.close()

            if not orders:
                print('None')


# In[ ]:




