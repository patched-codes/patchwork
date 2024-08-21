def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a int: The first number.
        b int: The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes an SQL query on the provided SQLite database and returns the result set.
    
    Args:
        db sqlite3.Connection: The connection to the SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map function: A function that maps items to a comparable key
        item1 any: The first item to compare
        item2 any: The second item to compare
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
