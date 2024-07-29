def a_plus_b(a, b):
    """A function that takes two numbers and returns their sum.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the SQLite database and fetches all results.
    
    Args:
        db <SQLite connection>: The SQLite database connection.
        query <str>: The query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the fetched results.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key map provided.
    
    Args:
        key_map function: A function that maps items to a comparable value.
        item1 Any: The first item to be compared.
        item2 Any: The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 if key_map(item1) == key_map(item2).
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
