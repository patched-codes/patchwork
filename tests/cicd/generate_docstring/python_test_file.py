def a_plus_b(a, b):
    """A function that calculates the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database connection and returns the results.
    
    Args:
        db <SQLite connection>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the mapping function provided.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
