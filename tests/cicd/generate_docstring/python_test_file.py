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
    """
    Executes the provided SQL query on the specified SQLite database and fetches all the results.
    
    Args:
        db <SQLite database connection>: The connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the fetched results from the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2, 
             0 if the keys are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
