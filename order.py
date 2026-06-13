import sqlite3
from datetime import datetime
from itertools import product

from validation import ValidationError


def Order_table():
    connect = sqlite3.connect('ecommerce.db')
    cursor = connect.cursor()

    cursor.execute('''
          create table if not exists orders(
             order_id text not null,
             customer_id text not null,
             order_date text not null,
             status text not null,
             total_amount real default 0,
             foreign key(customer_id) references customers(customer_id)
          )   
    ''')

    cursor.execute('''
          CREATE TABLE IF NOT EXISTS ORDER_ITEMS(
              order_item_id integer primary key autoincrement,
              order_id integer not null,
              product_id integer not null,
              quantity integer not null,
              price real not null,
              foreign key(order_id) references orders(order_id),
              foreign key(product_id) references orders(product_id)
          )    
    ''')
    connect.commit()
    connect.close()

def place_order(customer_id,items):
    connect = sqlite3.connect("ecommerce.db")
    cursor = connect.cursor()
    cursor.execute("select name from customers where customer_id=?",(customer_id))
    if not cursor.fetchone():
        connect.close()
        raise ValidationError("an order must contain at  least one item.")
    try:
        order_date =datetime.now().strftime("%y-%m-%d %H:%M:%S")

        status = "NEW"
        total_amount = 0
        cursor.execute('''
              insert into orders (customer_id,order_date,status,total_amount)
              values(?,?,?,?)
        ''',( customer_id,order_date,status,total_amount))
        order_id =cursor.lastrowid
        total_amount = 0

        for item in items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            if quantity <=0:
                raise ValidationError("quantity must be greater than 0.")

            cursor.execute("select price,stock from products where product_id=?",(product_id))

            product= cursor.fetchone()
            if not product:
                raise ValidationError(f"product{product_id} does not exist.")

            price,current_stock = product

            if current_stock < quantity:
                raise ValidationError(f"Insufficient stock for product{product_id}.Available:{current_stock}")

            new_stock = current_stock-quantity
            cursor.execute("update products set stock = ? where product_id=?",(new_stock,product_id))

            cursor.execute('''
                insert into order_items(order_id,product_id,quantity,price)
                values(?,?,?,?)
            ''',(order_id,product_id,quantity,price))

            total_amount +=price*quantity

            # update the calculated auto total amount
            cursor.execute("update order set total_amount= ? where order_id = ?",(total_amount,order_id))
            connect.commit()
            return {"status": "successfully","order_id":order_id,"total":total_amount}
    except Exception as e:
        raise e
    finally:
        connect.cursor()



def update_order_status(order_id,new_status):
    connect = sqlite3.connect("ecommerce.db")
    cursor = connect.cursor()


    cursor.execute("select status from orders where order_id = ?",(order_id,))
    order = cursor.fetchone()
    if not order:
        connect.close()
        raise ValidationError("order not found.")

    current_status = order[0]

    validate_order_status_transition(current_status,new_status)
    
    cursor.execute("update orders set status =? where order_id = ?",(new_status,order_id))
    connect.commit()
    connect.close()
    return {"status":f"order status update to {new_status}"}












            
            


    

        

    
