def a_plus_b(a, b):
    """This function adds two numbers and returns the result.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQLite query on the provided database.
    
    Args:
        db <SQLite connection>: The SQLite database connection.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the key values of two items based on a key map function.
    
    Args:
        key_map (function): A function that maps an item to a value used for comparison.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
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
