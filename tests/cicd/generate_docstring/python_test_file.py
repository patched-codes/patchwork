def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Query the SQLite database with the given query.
    
    Args:
        db <sqlite3.Connection>: The SQLite database connection.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all the rows retrieved by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the result of key_map function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: Input item 1 to be compared.
        item2: Input item 2 to be compared.
    
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
