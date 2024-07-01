def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the results.
    
    Args:
        db <SQLite connection>: Connection to the SQLite database.
        query <str>: SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key function provided.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
