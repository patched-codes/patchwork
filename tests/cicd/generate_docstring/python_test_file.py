def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQL query on a SQLite database and fetches all rows.
    
    Args:
        db <SQLite connection>: A connection to a SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing all rows fetched as a result of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the values mapped by a key function.
    
    Args:
        key_map function: A function that maps an item to a value for comparison.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
