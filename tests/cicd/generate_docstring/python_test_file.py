def a_plus_b(a, b):
    """This function adds two numbers a and b.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database and returns the result set.
    
    Args:
        db <SQLite Connection>: A connection to a SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        List of tuples: A list containing the rows fetched as tuples from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function provided in the key_map.
    
    Args:
        key_map (function): A function that maps an item to a comparable value.
        item1 (object): The first item to compare.
        item2 (object): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
