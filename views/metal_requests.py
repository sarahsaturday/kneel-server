import sqlite3
from models.metal import Metal

def get_all_metals():
    """
    Get all metals from the Metals table.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, metal, price
            FROM Metals
        """)

        metals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(row['id'], row['metal'], row['price'])
            metals.append(metal.__dict__)

    return metals

def get_single_metal(id):
    """
    Get a single metal by ID.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, metal, price
            FROM Metals
            WHERE id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        if row is not None:
            metal = Metal(row['id'], row['metal'], row['price'])
            return metal.__dict__
        else:
            return None

def create_metal(metal):
    """
    Create a new metal and add it to the Metals table.
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Metals (metal, price)
            VALUES (?, ?)
        """, (metal['metal'], metal['price']))

        id = db_cursor.lastrowid

        metal['id'] = id

    return metal

def delete_metal(id):
    """
    Delete metal
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Metals
            WHERE id = ?
        """, (id, ))

def update_metal(id, new_metal):
    """
    Update metal
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Metals
            SET metal = ?, price = ?
            WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
