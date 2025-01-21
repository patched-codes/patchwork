# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the queried data results fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (Callable[[Any], Comparable]): A function applied to the items for comparison, which returns a value that can be compared.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
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
    """Generates a random string of alphabets of a given length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A string consisting of random alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
