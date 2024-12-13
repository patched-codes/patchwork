# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on their mapped keys.
    
    Args:
        key_map (function): A function that takes an item and returns its key for comparison.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1's key is less than item2's key,
             1 if item1's key is greater than item2's key,
             0 if both keys are equal.
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
    """Generate a random string of alphabetic characters.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A random string consisting of alphabetic characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
