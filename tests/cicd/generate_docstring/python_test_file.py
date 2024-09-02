def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the provided SQLite database and returns all fetched results.
    
    Args:
        db (sqlite3.Connection): A connection object representing the SQLite database.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparable key from each item.
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
    Generate a random string of alphabets with a given length.
    
    Args:
        length (int): The length of the random alphabetic string to generate.
    
    Returns:
        str: A random string consisting of alphabetic characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))