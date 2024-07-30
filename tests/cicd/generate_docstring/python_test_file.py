def a_plus_b(a, b):
    """This function returns the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the given SQLite database and returns the result.
    
    Args:
        db <SQLite Connection>: Connection to the SQLite database.
        query <str>: SQL query to be executed.
    
    Returns:
        list: List of tuples containing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the provided key_map function.
    
    Args:
        key_map function: A function that maps an item to a value for comparison.
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
