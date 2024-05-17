import sqlite3

database = "app.db"

conn = sqlite3.connect(database)
cursor = conn.cursor()


script = ""

# Ініціалізація таблиць
def init_tables():
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    );
        
    CREATE TABLE IF NOT EXISTS customers ( 
        customer_id INTEGER PRIMARY KEY, 
        first_name TEXT NOT NULL, 
        last_name TEXT NOT NULL, 
        email TEXT NOT NULL UNIQUE 
    );
                       
    CREATE TABLE IF NOT EXISTS orders ( 
        order_id INTEGER PRIMARY KEY, 
        customer_id INTEGER NOT NULL, 
        product_id INTEGER NOT NULL, 
        quantity INTEGER NOT NULL, 
        order_date DATE NOT NULL, 
        
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
        FOREIGN KEY (product_id) REFERENCES products(product_id) 
    );
    """)
    conn.commit()


# SQL-запити
def add_product(name, category, price):
    global script
    query = f"""
    INSERT INTO products (name, category, price) VALUES ("{name}", "{category}", {price});
    """
    script += query

def add_customer(first_name, last_name, email):
    global script
    query = f"""
    INSERT INTO customers (first_name, last_name, email) VALUES ("{first_name}", "{last_name}", "{email}");
    """
    script += query

def add_order(customer_id, product_id, quantity):
    global script
    query = f"""
    INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES ({customer_id}, {product_id}, {quantity}, CURRENT_DATE);
    """
    script += query

def update_price_in_category(category, procentage):
    global script
    query = f"""
    UPDATE products SET price = price + price / 100 * {procentage} WHERE category = "{category}"
    """
    script += query

def get_total_income():
    cursor.execute("""
    SELECT SUM(products.price * orders.quantity) AS total
    FROM orders 
    JOIN products ON orders.product_id = products.product_id;
    """)

    return cursor.fetchall()[0]

def get_orders_count():
    cursor.execute("""
    SELECT customers.customer_id, COUNT(orders.customer_id) as orders
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_id
    """)

    return cursor.fetchall()

def get_avarage_order_price():
    cursor.execute("""
    SELECT AVG(orders.quantity * products.price)
    FROM orders
    INNER JOIN products ON orders.product_id = products.product_id;
    """)

    return cursor.fetchall()[0]

def get_most_popular_category():
    cursor.execute("""
    SELECT p.category, COUNT(o.order_id) AS num_orders
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category
    ORDER BY num_orders DESC
    LIMIT 1;
    """)

    return cursor.fetchall()

def get_product_amount_in_categories():
    cursor.execute("""
    SELECT products.category, COUNT(products.category)
    FROM products
    GROUP BY products.category;
    """)

# 
def clear_script():
    global script
    script = ""

def save():
    cursor.executescript(script)
    conn.commit()
    clear_script()


def close():
    cursor.close()
    conn.close()

# cursor.execute("""
#     SELECT SUM(products.price * orders.quantity) AS total
# FROM orders 
# JOIN products ON orders.product_id = products.product_id;
# """)

# print(cursor.fetchall())

# cursor.execute("""
# SELECT customers.customer_id, COUNT(orders.customer_id) as orders
# FROM customers
# INNER JOIN orders ON customers.customer_id = orders.customer_id
# GROUP BY customers.customer_id
# """)

# print(cursor.fetchall())

# cursor.execute("""
# SELECT AVG(orders.quantity * products.price)
# FROM orders
# INNER JOIN products ON orders.product_id = products.product_id;
# """)

# print(cursor.fetchall())


# # cursor.execute("""
# # SELECT products.category, COUNT(products)
# # """)