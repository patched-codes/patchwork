def a_plus_b(a, b):
    """
    Adds two numbers together.
    
    Args:
        a int: The first number to be added.
        b int: The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes the given query on the SQLite database and returns all the results.
    
    Args:
        db connection: A connection object to the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing all the rows fetched as a result of the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps the items to a comparable value.
        item1: Any type. The first item to be compared.
        item2: Any type. The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if greater, and 0 if equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
