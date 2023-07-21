import sqlite3
from models.style import Style

def get_all_styles():
    """
    Get all styles from the Styles table.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, style, price
            FROM Styles
        """)

        styles = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            style = Style(row['id'], row['style'], row['price'])
            styles.append(style.__dict__)

    return styles

def get_single_style(id):
    """
    Get a single style by ID.

    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, style, price
            FROM Styles
            WHERE id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        if row is not None:
            style = Style(row['id'], row['style'], row['price'])
            return style.__dict__
        else:
            return None

def create_style(style):
    """
    Create a new style and add it to the Styles table.
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Styles (style, price)
            VALUES (?, ?)
        """, (style['style'], style['price']))

        id = db_cursor.lastrowid

        style['id'] = id

    return style

def delete_style(id):
    """
    Delete style
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Styles
            WHERE id = ?
        """, (id, ))

def update_style(id, new_style):
    """
    Update style
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Styles
            SET style = ?, price = ?
            WHERE id = ?
        """, (new_style['style'], new_style['price'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
