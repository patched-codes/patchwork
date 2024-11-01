# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a query on a SQLite database and returns all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a key to be compared.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal based on the key map.
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
    """Generate a random string of alphabets of specified length.
    
    Args:
        length int: The length of the random alphabet string to be generated.
    
    Returns:
        str: A string consisting of random alphabetical characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
