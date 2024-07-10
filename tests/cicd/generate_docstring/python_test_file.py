def a_plus_b(a, b):
    """This function returns the sum of two input numbers.
    
    Args:
        a (int): The first input number.
        b (int): The second input number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a query on the provided SQLite database and return the results.
    
    Args:
        db <SQLite connection>: The connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all rows retrieved from the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on the key_map function.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
