import sqlite3
import uuid
from validation import validate_customer,ValidationError


def customer_table():
    connect= sqlite3.connect("ecommerce.db")
    cursor= connect.cursor()
    cursor.execute('''
          create table if not exists customers(
           customer_id text primary key,
           name text not null,
           email text unique not null,
           phone text not null,
           city text not null,
           created_at timestamp default current_timestamp
          ) 
    ''')
    connect.commit()
    connect.close()
    
def create_customer(name,email,phone,city):
    connect= sqlite3.connect('ecommerce.db')
    cursor= connect.cursor()
    customer_id = str(uuid.uuid4())
    cursor.execute(
        "insert into customers values(?,?,?,?,?current_timestamp)",
        (customer_id,name,email,phone,city)
    )
    connect.commit()
    connect.close()

    return customer_id

d1=create_customer()


