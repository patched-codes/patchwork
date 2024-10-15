def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a provided SQLite database and retrieves all results.
    
    Args:
        db sqlite3.Connection: A connection object that represents the SQLite database.
        query str: The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing all rows returned by the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that extracts a key from an item for comparison.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
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
        length (int): The number of alphabets to generate in the string.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
