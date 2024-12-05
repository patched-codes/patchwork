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
    """Executes a given SQL query on a SQLite database and returns all the results.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list containing all rows of the query result. Each row is represented as a tuple.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key derived from a key mapping function.
    
    Args:
        key_map (callable): A function that takes an item and returns a key to compare.
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
    """Generates a random string of alphabets of specified length.
    
    Args:
        length (int): The number of random alphabetic characters to generate.
    
    Returns:
        str: A string composed of random alphabetic characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
