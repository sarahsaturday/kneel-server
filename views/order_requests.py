"""
This module provides orders stuff
"""
ORDERS = [
    {
        "metalId": 1,
        "sizeId": 2,
        "styleId": 2,
        "id": 1
    },
    {
        "metalId": 3,
        "sizeId": 3,
        "styleId": 3,
        "id": 2
    },
    {
        "metalId": 2,
        "sizeId": 1,
        "styleId": 3,
        "id": 3
    },
    {
        "metalId": 1,
        "sizeId": 3,
        "styleId": 3,
        "id": 4
    },
    {
        "metalId": 3,
        "sizeId": 3,
        "styleId": 3,
        "id": 5
    },
    {
        "metalId": 2,
        "sizeId": 2,
        "styleId": 1,
        "id": 6
    },
    {
        "metalId": 5,
        "sizeId": 4,
        "styleId": 3,
        "id": 7
    },
    {
        "metalId": 3,
        "sizeId": 4,
        "styleId": 3,
        "id": 8
    }
]


def get_all_orders():
    """
    Get all orders.

    """
    return ORDERS

def get_single_order(id):
    """
    Get a single order by ID.

    """
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    """
    Create a new order and add it to the list of ORDERS.

    """
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    """
    delete order

    """
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """
    update order

    """
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
