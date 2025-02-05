# fmt: off
def a_plus_b(a, b):
    """Compute the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and returns an integer based on their comparison.
    
    Args:
        key_map function: A function applied to each item to extract a comparison key.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, or 0 if item1 == item2.
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
    """Generates a random string of alphabetic characters of a specified length.
    
    Args:
        length (int): The length of the random alphabetic string to generate.
    
    Returns:
        str: A string composed of random alphabetic characters of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
