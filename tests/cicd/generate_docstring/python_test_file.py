def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on a sqlite database and return the result.
    
    Args:
        db <sqlite3.Connection>: A connection to a sqlite database.
        query <str>: The SQL query to execute.
    
    Returns:
        list: A list containing all rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key map provided.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
