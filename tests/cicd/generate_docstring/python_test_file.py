def a_plus_b(a, b):
    """Returns the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on a SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key extracted from them.
    
    Args:
        key_map (function): A function that extracts a comparison key from an item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, 0 if items are equal based on the comparison key.
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
        length int: The number of characters in the generated string.
    
    Returns:
        str: A string consisting of random alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
