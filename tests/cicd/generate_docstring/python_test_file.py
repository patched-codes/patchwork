def a_plus_b(a, b):
    """Function to add two numbers.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the results.
    
    Args:
        db <SQLite connection>: A connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
