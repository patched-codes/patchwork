# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Execute a SQL query on the provided SQLite database and return all fetched results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute on the database.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a key function and returns an integer based on their comparison.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if item1 should come before item2, 1 if item1 should come after item2, and 0 if they are considered equal.
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
    """Generate a random string of alphabets of a given length.
    
    Args:
        length (int): The desired length of the generated string.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
