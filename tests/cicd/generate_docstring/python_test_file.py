def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a query on a SQLite database and fetch all the results.
    
    Args:
        db <SQLite Connection object>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all the rows fetched as a result of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on their keys mapped by a given function.
    
    Args:
        key_map (function): A function that maps an item to a key for comparison.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2),
             and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
