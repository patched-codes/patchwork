def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a query on a SQLite database using the provided cursor and returns all the results.
    
    Args:
        db <SQLite connection>: A connection to a SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all the rows fetched as a result of the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
