# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a query on an SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a specified key mapping function and returns an integer based on their comparison.
    
    Args:
        key_map Callable: A function used to extract a comparison key from each item.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: Returns -1 if the key from item1 is less than the key from item2, 1 if it is greater, and 0 if they are equal.
    """
    
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0


def random_alphabets(
        length: int
):
    """Generates a random string of alphabets of specified length.
    
    Args:
        length int: The length of the random alphabetic string to be generated.
    
    Returns:
        str: A string consisting of randomly chosen alphabetic characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
