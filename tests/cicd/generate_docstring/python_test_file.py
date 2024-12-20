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
    """Executes a SQL query on the given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): An SQLite database connection object.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the result set from the executed query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and returns an integer based on their ordering.
    
    Args:
        key_map (Callable): A function that extracts a key from each item for comparison.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal based on the key function.
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
    """Generate a random string of alphabets.
    
    Args:
        length (int): The length of the resulting string of random alphabets.
    
    Returns:
        str: A string composed of randomly chosen alphabets with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
