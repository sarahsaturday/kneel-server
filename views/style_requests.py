"""
This module provides style stuff
"""
STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]


def get_all_styles():
    """
    Get all styles.

    """
    return STYLES

def get_single_style(id):
    """
    Get a single style by ID.

    """
    # Variable to hold the found style, if it exists
    requested_style = None

    # Iterate the STYLES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style

def create_style(style):
    """
    Create a new style and add it to the list of STYLES.

    """
    # Get the id value of the last style in the list
    max_id = STYLES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the style dictionary
    style["id"] = new_id

    # Add the style dictionary to the list
    STYLES.append(style)

    # Return the dictionary with `id` property added
    return style

def delete_style(id):
    """
    delete style

    """
    # Initial -1 value for style index, in case one isn't found
    style_index = -1

    # Iterate the STYLES list, but use enumerate() so that you
    # can access the index value of each item
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the style. Store the current index.
            style_index = index

    # If the style was found, use pop(int) to remove it from list
    if style_index >= 0:
        STYLES.pop(style_index)

def update_style(id, new_style):
    """
    update style

    """
    # Iterate the STYLES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the style. Update the value.
            STYLES[index] = new_style
            break
