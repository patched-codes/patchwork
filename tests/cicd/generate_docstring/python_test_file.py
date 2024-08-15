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
    """Executes an SQL query on a SQLite database and returns the result set.
    
    Args:
        db <sqlite3.Connection>: A connection to a SQLite database.
        query str: The SQL query to be executed.
    
    Returns:
        List: A list of rows representing the result set of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the key function provided in the key_map.
    
    Args:
        key_map (function): A function that returns the key to be compared for each item.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
