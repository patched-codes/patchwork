# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on the provided SQLite database and retrieves all results.
    
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
    """Compares two items based on a key extracted from them using the provided key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a key for comparison.
        item1 (object): The first item to compare.
        item2 (object): The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2,
             1 if the key of item1 is greater than the key of item2,
             0 if the keys are equal.
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
    """Generate a random string of alphabetic characters of a specified length.
    
    Args:
        length int: The length of the random alphabetic string to generate.
    
    Returns:
        str: A string consisting of randomly selected alphabetic characters (both uppercase and lowercase) with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
