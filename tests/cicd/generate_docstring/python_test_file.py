# fmt: off
def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the given SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list of tuple: A list containing tuples of the query results.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on their keys obtained via the key_map function.
    
    Args:
        key_map (Callable): A function that extracts a key from the items for comparison.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2,
             returns 1 if the key of item1 is greater than the key of item2,
             and returns 0 if the keys are equal.
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
    """Generates a random string of alphabets.
    
    Args:
        length (int): The length of the random string to generate.
    
    Returns:
        str: A random string consisting of alphabetic characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
