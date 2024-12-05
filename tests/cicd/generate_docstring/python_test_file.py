# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQL query on the given SQLite database and fetches all the results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): An SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned from the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted from each by applying a key mapping function.
    
    Args:
        key_map function: A function that extracts a key from each item for comparison.
        item1 Any: The first item to be compared.
        item2 Any: The second item to be compared.
    
    Returns:
        int: Returns -1 if item1's key is less than item2's key, 1 if item1's key is greater, and 0 if they are equal.
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
    """Generate a random string of alphabets with a specified length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A string consisting of random alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
