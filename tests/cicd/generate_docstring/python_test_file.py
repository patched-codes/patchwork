def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the fetched results.
    
    Args:
        db <SQLite connection>: Connection to a SQLite database.
        query <str>: SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the fetched results from the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key map function provided.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2),
             or 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
