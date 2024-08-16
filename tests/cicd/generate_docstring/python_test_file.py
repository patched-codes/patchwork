def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the results.
    
    Args:
        db object: A connection object to the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2), 
             0 if key_map(item1) is equal to key_map(item2).
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
