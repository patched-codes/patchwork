# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a query on a given SQLite database connection and fetch all results.
    
    Args:
        db (sqlite3.Connection): A connection object that represents the SQLite database.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows returned from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (Callable): A function that takes an item and returns a value to compare.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
    """Generates a random string of alphabets with a specified length.
    
    Args:
        length (int): The desired length of the random string.
    
    Returns:
        str: A random string composed of uppercase and lowercase English alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
