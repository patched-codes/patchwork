def a_plus_b(a, b):
    """A function that performs addition of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQLite query on the provided database connection.
    
    Args:
        db <connection>: A sqlite3 database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the query result.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
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
