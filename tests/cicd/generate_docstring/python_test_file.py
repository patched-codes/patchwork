def a_plus_b(a, b):
    """This function adds two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on the specified SQLite database and return the results.
    
    Args:
        db: SQLite database connection.
        query (str): SQL query to be executed.
    
    Returns:
        list: A list containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key map function.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1: The first item to be compared.
        item2: The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
