def a_plus_b(a, b):
    """
    A function that calculates the sum of two numbers.
    
    Args:
        a int/float: The first number to be added.
        b int/float: The second number to be added.
    
    Returns:
        int/float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the provided SQLite database and returns all the results.
    
    Args:
        db <SQLite connection>: A connection to the SQLite database.
        query <str>: The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the query results.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the key values of two items using a key mapping function.
    
    Args:
        key_map function: A function that maps an item to a key value.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: Returns -1 if key value of item1 is less than key value of item2, 
             1 if key value of item1 is greater than key value of item2, 
             and 0 if key values are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
