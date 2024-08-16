def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute an SQLite query on the given database and return the result.
    
    Args:
        db <SQLite connection>: The SQLite database connection.
        query <str>: The query to be executed on the database.
    
    Returns:
        list: A list containing the rows fetched as a result of the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1 : Any: The first item to compare.
        item2 : Any: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2),
             0 if key_map(item1) is equal to key_map(item2).
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
