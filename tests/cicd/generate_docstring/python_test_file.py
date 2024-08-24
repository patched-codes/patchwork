def a_plus_b(a, b):
    """This function computes the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the SQLite database and returns the results.
    
    Args:
        db <connection object>: A connection object to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing the rows of the result set.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the key values of two items using the provided key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
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
