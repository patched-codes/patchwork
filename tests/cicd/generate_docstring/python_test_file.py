def a_plus_b(a, b):
    """A function that adds two numbers.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database connection and returns all rows.
    
    Args:
        db <sqlite3.Connection>: A connection to a SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key_map function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2), 1 if key_map(item1) is greater than key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
