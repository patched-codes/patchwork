def a_plus_b(a, b):
    """A function that adds two numbers.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database and returns the result.
    
    Args:
        db <sqlite3.Connection>: A connection object representing a SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map (function): A function that maps an item to a comparable key.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: -1 if key of item1 is less than key of item2, 1 if key of item1 is greater than key of item2, 0 if keys are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
