def a_plus_b(a, b):
    """Function to add two numbers.
    
    Args:
        a (int): First number to be added.
        b (int): Second number to be added.
    
    Returns:
        int: Sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQL query on a SQLite database and returns the results.
    
    Args:
        db <SQLite Connection>: A connection to the SQLite database.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key map function.
    
    Args:
        key_map (function): A function that maps an item to a value for comparison.
        item1 (object): The first item to compare.
        item2 (object): The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) is less than key_map(item2),
             1 if key_map(item1) is greater than key_map(item2),
             0 if key_map(item1) is equal to key_map(item2).
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
