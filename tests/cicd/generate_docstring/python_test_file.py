def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes the given SQL query on the provided SQLite database and returns all rows.
    
    Args:
        db <SQLite Connection>: A connection object to an SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all rows returned by the SQL query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a key map function.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
