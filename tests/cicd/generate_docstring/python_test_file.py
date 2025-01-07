# fmt: off
def a_plus_b(a, b):
    """Adds two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a provided SQLite database connection and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object to execute the query on.
        query (str): The SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows retrieved by the query execution.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a comparable key.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
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
    """Generates a random string of alphabets.
    
    Args:
        length (int): The length of the random alphabetic string to generate.
    
    Returns:
        str: A random string composed of ASCII letters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
