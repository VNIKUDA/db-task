import sqlite3

database = "app.db"

conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
    SELECT SUM(products.price * orders.quantity) AS total
FROM orders 
JOIN products ON orders.product_id = products.product_id;
""")

print(cursor.fetchall())

cursor.execute("""
SELECT customers.customer_id, COUNT(orders.customer_id) as orders
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
""")

print(cursor.fetchall())

cursor.execute("""
SELECT AVG(orders.quantity * products.price)
FROM orders
INNER JOIN products ON orders.product_id = products.product_id;
""")

print(cursor.fetchall())


# cursor.execute("""
# SELECT products.category, COUNT(products)
# """)