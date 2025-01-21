# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (numeric): The first number.
        b (numeric): The second number.
    
    Returns:
        numeric: The sum of the two numbers a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a specified key mapping function.
    
    Args:
        key_map callable: A function that maps an item to its key for comparison.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 < item2, 1 if item1 > item2, or 0 if they are equal.
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
    """Generates a random string of alphabetic characters of specified length.
    
    Args:
        length (int): The number of random alphabetic characters to generate.
    
    Returns:
        str: A string composed of random alphabetic characters of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
