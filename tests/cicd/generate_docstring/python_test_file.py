def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on the provided SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a specified key mapping function.
    
    Args:
        key_map (function): A function that extracts the key from an item for comparison.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
    Returns:
        int: -1 if item1's key is less than item2's key, 1 if greater, and 0 if equal.
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
    Generates a random string of alphabets of the specified length.
    
    Args:
        length int: The length of the random string to generate.
    
    Returns:
        str: A random string composed of ASCII letters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
