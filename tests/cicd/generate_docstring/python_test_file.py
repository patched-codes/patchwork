# fmt: off
def a_plus_b(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples where each tuple represents a row in the query result.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted by a key mapping function.
    
    Args:
        key_map function: A function that extracts a comparison key from an item.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
    """Generates a random string of alphabetic characters with the specified length.
    
    Args:
        length (int): The desired length of the random string.
    
    Returns:
        str: A random string of alphabetic characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
