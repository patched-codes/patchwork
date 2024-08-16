def a_plus_b(a, b):
    """A function that adds two numbers.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the provided SQLite database and returns the result set.
    
    Args:
        db sqlite3.Connection: A connection object representing the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        List: A list of tuples representing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 : The first item to be compared.
        item2 : The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
