def a_plus_b(a, b):
    """Performs addition of two numbers.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes the provided query on the given SQLite database and returns the result as a list of tuples.
    
    Args:
        db <sqlite3.Connection>: An SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the mapping function specified in key_map.
    
    Args:
        key_map (function): A function that maps items to a value for comparison.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
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
