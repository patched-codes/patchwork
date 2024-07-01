def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on a SQLite database and fetch all results.
    
    Args:
        db <SQLite connection>: A connection to the SQLite database.
        query <str>: The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the fetched results.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that retrieves the key to compare from an item.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: 
            -1 if key_map(item1) < key_map(item2)
            1 if key_map(item1) > key_map(item2)
            0 if key_map(item1) == key_map(item2)
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
