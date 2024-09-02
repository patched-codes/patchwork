def a_plus_b(a, b):
    """Add two numbers together.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQLite query and fetch all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing all the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (callable): A function that extracts a comparable key from the items.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, 0 if item1 == item2.
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
    """
    Generate a random string of alphabetic characters.
    
    Args:
        length (int): The desired length of the random string.
    
    Returns:
        str: A string of random alphabetic characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))