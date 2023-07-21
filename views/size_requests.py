import sqlite3
from models.size import Size

def get_all_sizes():
    """
    Get all sizes from the Sizes table.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, carets, price
            FROM Sizes
        """)

        sizes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Size(row['id'], row['carets'], row['price'])
            sizes.append(size.__dict__)

    return sizes

def get_single_size(id):
    """
    Get a single size by ID.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, carets, price
            FROM Sizes
            WHERE id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        if row is not None:
            size = Size(row['id'], row['carets'], row['price'])
            return size.__dict__
        else:
            return None

def create_size(size):
    """
    Create a new size and add it to the Sizes table.
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Sizes (carets, price)
            VALUES (?, ?)
        """, (size['carets'], size['price']))

        id = db_cursor.lastrowid

        size['id'] = id

    return size

def delete_size(id):
    """
    Delete size
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Sizes
            WHERE id = ?
        """, (id, ))

def update_size(id, new_size):
    """
    Update size
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Sizes
            SET carets = ?, price = ?
            WHERE id = ?
        """, (new_size['carets'], new_size['price'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
