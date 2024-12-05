# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows fetched from the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that extracts a key from an item for comparison purposes.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length int: The number of random alphabets to generate.
    
    Returns:
        str: A random string consisting of alphabetic characters with the given length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
