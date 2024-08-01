def a_plus_b(a, b):
    """This function calculates the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on the given SQLite database and returns the result.
    
    Args:
        db <SQLite connection>: The SQLite database connection to execute the query on.
        query <str>: The SQL query to be executed.
    
    Returns:
        list: A list containing all the rows fetched as a result of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares the key values of two items based on the provided key map function.
    
    Args:
        key_map function: A function that retrieves the key value from an item.
        item1: The first item to compare.
        item2: The second item to compare.
    
    Returns:
        int: -1 if key value of item1 is less than key value of item2, 1 if key value of item1 is greater than key value of item2, 0 if key values are equal.
    """
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0
