def a_plus_b(a, b):
    """Return the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the result set.
    
    Args:
        db <SQLite connection>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that extracts the comparable key from an item.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
