def a_plus_b(a, b):
    """Returns the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the specified SQLite database and returns the results.
    
    Args:
        db : database connection object
        query : str: SQL query to be executed
    
    Returns:
        list: Results of the query as a list of tuples
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key mapping function provided.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
