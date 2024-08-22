def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """
    Executes the provided SQL query on the given SQLite database and returns all the results.
    
    Args:
        db <SQLite Connection>: A connection to the SQLite database.
        query <str>: The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a provided key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
