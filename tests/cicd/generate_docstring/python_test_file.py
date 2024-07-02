def a_plus_b(a, b):
    """A function that adds two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """This function executes a SQL query on a SQLite database and fetches all the results.
    
    Args:
        db <SQLite Connection>: A connection object to the SQLite database.
        query <str>: The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing all the rows fetched by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on the result of a key mapping function.
    
    Args:
        key_map function: A function that maps an item to a comparable value.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
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
