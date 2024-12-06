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
    """Executes a SQL query on a SQLite database and retrieves the results.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples representing rows fetched from the database, as returned by the `fetchall()` method.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted via a key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparable key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, 
        and 0 if the keys of both items are equal.
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
    """Generate a random string of alphabets with a specified length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A string consisting of random alphabetic characters of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
