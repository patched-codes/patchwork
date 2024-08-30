def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int/float): The first number.
        b (int/float): The second number.
    
    Returns:
        int/float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on an SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a provided key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: -1 if the first item is less than the second, 1 if the first item is greater than the second, and 0 if they are equal.
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
    Generate a random string of alphabets of a specified length.
    
    Args:
        length int: The length of the random string to generate.
    
    Returns:
        str: A random string of alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))