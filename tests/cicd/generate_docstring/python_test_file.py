def a_plus_b(a, b):
    """A function that takes two inputs and returns their sum.
    
    Args:
        a (int): The first input.
        b (int): The second input.
    
    Returns:
        int: The sum of the two inputs.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns the results.
    
    Args:
        db <SQLite connection>: The connection to the SQLite database.
        query <str>: The query to be executed on the database.
    
    Returns:
        list: A list containing all the rows fetched from the database as a result of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that maps items to comparable keys.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        integer: 
            -1 if key_map(item1) is less than key_map(item2)
            1 if key_map(item1) is greater than key_map(item2)
            0 if key_map(item1) is equal to key_map(item2)
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
