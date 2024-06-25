def a_plus_b(a, b):
    """This function returns the sum of two input numbers.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the provided SQLite database and returns the result.
    
    Args:
        db <SQLite database connection>: The database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that takes an item and returns a key for comparison.
        item1 : The first item to compare.
        item2 : The second item to compare.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2), 1 if greater, and 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
