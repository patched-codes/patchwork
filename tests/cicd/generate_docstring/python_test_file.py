def a_plus_b(a, b):
    """This function takes two input parameters and returns their sum.
    
    Args:
        a int: The first input integer.
        b int: The second input integer.
    
    Returns:
        int: The sum of the two input integers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQLite query on the given database and fetches all the results.
    
    Args:
        db <SQLite connection>: The SQLite database connection.
        query <str>: The query to be executed.
    
    Returns:
        list: A list containing all the rows fetched by executing the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a given key map function.
    
    Args:
        key_map function: A function that extracts the key for comparison from an item.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if key_map(item1) < key_map(item2), 1 if key_map(item1) > key_map(item2), 0 if they are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
