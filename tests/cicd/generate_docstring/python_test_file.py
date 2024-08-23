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
    """Executes a query on the SQLite database and returns all results.
    
    Args:
        db <SQLite Connection>: An SQLite database connection object.
        query <str>: A SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing all rows fetched from the database as a result of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key mapping function.
    
    Args:
        key_map function: A function that maps an item to a key for comparison.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: 
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
