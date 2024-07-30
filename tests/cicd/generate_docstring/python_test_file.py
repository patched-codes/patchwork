def a_plus_b(a, b):
    """This function returns the sum of two input numbers.
    
    Args:
        a (int): The first input number.
        b (int): The second input number.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the SQLite database and returns all the results.
    
    Args:
        db <connection object>: Connection object to the SQLite database
        query <string>: SQL query to be executed
    
    Returns:
        list: A list of tuples containing all the rows fetched from the database
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: Returns -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2),
             and 0 if key_map(item1) is equal to key_map(item2).
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
