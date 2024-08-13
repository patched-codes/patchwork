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
    """Executes a query on the SQLite database and returns the result.
    
    Args:
        db SQLite connection: The connection to the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list containing all rows of the query result.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 Any: The first item to be compared.
        item2 Any: The second item to be compared.
    
    Returns:
        int: Returns -1 if the first item is less than the second, 1 if the first item is greater than the second, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
