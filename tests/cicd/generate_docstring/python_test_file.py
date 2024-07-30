def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the given SQLite database and returns the result set.
    
    Args:
        db <SQLite connection>: The connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all rows of the result set.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function to extract a key from an item.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
