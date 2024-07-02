def a_plus_b(a, b):
    """A simple function that adds two numbers.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQLite query on the database and returns the results.
    
    Args:
        db <connection>: The SQLite database connection.
        query <str>: The query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the mapped values of two items based on the key_map function.
    
    Args:
        key_map function: A function that maps an item to a value for comparison.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if the mapped value of item1 is less than the mapped value of item2,
             1 if the mapped value of item1 is greater than the mapped value of item2,
             0 if the mapped values of item1 and item2 are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
