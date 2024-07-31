def a_plus_b(a, b):
    """A function that adds two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQLite query on the database and returns the result.
    
    Args:
        db <SQLite Connection>: A connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing the rows of the result set returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a value for comparison.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: -1 if the value of item1 is less than the value of item2, 1 if the value of item1 is greater than the value of item2, 0 if both values are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
