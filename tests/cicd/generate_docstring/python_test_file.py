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
    """
    Executes the given query on the SQLite database and returns all rows.
    
    Args:
        db <SQLiteConnection>: The SQLite database connection.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the given key map function.
    
    Args:
        key_map function: A function that maps an item to a comparable key value.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
