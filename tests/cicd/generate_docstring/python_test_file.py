def a_plus_b(a, b):
    """A function that adds two numbers.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute the provided SQLite query on the given database connection and return the results.
    
    Args:
        db <connection>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all the rows fetched as a result of the query execution.
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
        int: Returns -1 if item1 is smaller than item2, 1 if item1 is larger than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
