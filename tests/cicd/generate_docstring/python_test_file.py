def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes the given query on the provided SQLite database and returns the result.
    
    Args:
        db <SQLite connection>: The SQLite database connection object.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all rows as tuples that match the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key map function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
