def a_plus_b(a, b):
    """A function that adds two input numbers.
    
    Args:
        a int: The first input number.
        b int: The second input number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the provided SQLite database and returns the result set.
    
    Args:
        db sqlite3.Connection: A connection to the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        List: A list of tuples representing the rows fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1: The first item to compare.
        item2: The second item to compare.
    
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
