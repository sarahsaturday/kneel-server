import sqlite3
from models.order import Order

def get_all_orders():
    """
    Get all orders from the Orders table, including expanded data from related tables.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT o.id, o.metal_id, o.size_id, o.style_id, m.metal, m.price,
                s.carets, s.price, st.style, st.price
            FROM Orders o
            JOIN Metals m ON m.id = o.metal_id
            JOIN Sizes s ON s.id = o.size_id
            JOIN Styles st ON st.id = o.style_id
        """)

        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            # Construct the order with the appropriate arguments
            order = Order(
                row['id'],
                row['metal_id'],
                row['size_id'],
                row['style_id'],
                row['metal'],
                row['price'],  # Use the correct key for price from Metals table
                row['carets'],
                row['price'],  # Use the correct key for price from Sizes table
                row['style'],
                row['price']  # Use the correct key for price from Styles table
            )

            # You can create a dictionary for metal, size, and style
            metal = {
                'id': row['id'],
                'metal': row['metal'],
                'price': row['price']
            }

            size = {
                'id': row['id'],
                'carets': row['carets'],
                'price': row['price']
            }

            style = {
                'id': row['id'],
                'style': row['style'],
                'price': row['price']
            }

            # Assign the dictionaries for metal, size, and style to the Order instance
            order.metal = metal
            order.size = size
            order.style = style

            # Add the dictionary representation of the order to the list
            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """
    Get a single order by ID.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT o.id, m.metal, s.carets, st.style, m.price AS metal_price, s.price AS size_price, st.price AS style_price
            FROM Orders o
            JOIN Metals m ON m.id = o.metal_id
            JOIN Sizes s ON s.id = o.size_id
            JOIN Styles st ON st.id = o.style_id
            WHERE o.id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        if row is not None:
            # Construct the order with the appropriate arguments
            order = Order(
                row['id'],
                row['metal_id'],
                row['size_id'],
                row['style_id'],
                row['metal'],
                row['metal_price'],  # Make sure to use the correct key for price from Metals table
                row['carets'],
                row['size_price'],
                row['style'],
                row['style_price']  # Make sure to use the correct key for price from Styles table
            )
            return order.__dict__
        else:
            return None

def create_order(new_order):
    """
    Create a new order and add it to the Orders table.
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Orders (metal_id, size_id, style_id)
            VALUES (?, ?, ?)
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id']))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order

def delete_order(id):
    """
    Delete order
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Orders
            WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """
    Update order
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Orders
            SET metal_id = ?, size_id = ?, style_id = ?
            WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
