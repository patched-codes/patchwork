def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the provided SQLite database connection and returns all the results.
    
    Args:
        db <sqlite3.Connection>: The SQLite database connection.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps items to a key for comparison.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
