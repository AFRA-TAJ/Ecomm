#!/usr/bin/env python
# coding: utf-8

# In[1]:


from UTIL.DBPropertyUtil import PropertyUtil

import mysql.connector as sql

class DbConnect():
    def __init__(self):
        pass

    def open(self):
        print("Opening database connection...")  # Add this line
        try:
            l = PropertyUtil.getPropertyString()
            self.conn = sql.connect(host=l[0], user=l[1], password=l[2], database=l[3])
            if self.conn:
                print("Database Is Connected")
            self.stmt = self.conn.cursor()
        except sql.Error as e:
            print(f"Error connecting to the database: {e}")

    def close(self):
        self.conn.close()


# In[ ]:




