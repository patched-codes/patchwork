def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.
    
    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Execute a SQL query on a given SQLite database and return the fetched results.
    
    Args:
        db sqlite3.Connection: The SQLite database connection object.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched from the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on their mapped values and returns an order indicator.
    
    Args:
        key_map (function): A function that maps an item to a comparable value.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: -1 if the mapped value of item1 is less than the mapped value of item2,
             1 if the mapped value of item1 is greater than the mapped value of item2,
             0 if the mapped values of item1 and item2 are equal.
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
    Generate a random string of alphabetic characters of a given length.
    
    Args:
        length int: The desired length of the random alphabetic string.
    
    Returns:
        str: A random string composed of alphabetic characters (both uppercase and lowercase) with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))