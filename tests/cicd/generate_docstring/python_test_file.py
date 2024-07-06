def a_plus_b(a, b):
    """Function to add two numbers.
    
    Args:
        a int: The first integer.
        b int: The second integer.
    
    Returns:
        int: The sum of the two integers.
    """
    return a + b


def sqlite(db, query):
    """Execute a query on a SQLite database and return all results.
    
    Args:
        db <SQLite connection>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing all rows fetched by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key function provided in the key_map.
    
    Args:
        key_map function: A function that maps items to a comparable key.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
