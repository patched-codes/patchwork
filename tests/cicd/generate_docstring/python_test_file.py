def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a query on a SQLite database and return the results.
    
    Args:
        db <SQLite Connection>: The SQLite database connection.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing the rows resulting from the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
