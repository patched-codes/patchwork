def a_plus_b(a, b):
    """This function returns the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute an SQL query on a SQLite database and return the results.
    
    Args:
        db <sqlite3.Connection>: The connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the result rows of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the items based on a specified key mapping function.
    
    Args:
        key_map function: A function that maps the items to a comparable key value.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
