def a_plus_b(a, b):
    """This function returns the sum of two numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes the given SQL query on the database and returns the results.
    
    Args:
        db <database connection>: The connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows retrieved from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the mapping function provided.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 otherwise.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
