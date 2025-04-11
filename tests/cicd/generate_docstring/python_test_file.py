# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided SQLite database connection and returns the results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): A SQL query string to execute on the database.
    
    Returns:
        list: A list of tuples containing the result set of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function and returns an integer for sorting purposes.
    
    Args:
        key_map function: A function applied to each item to extract comparison keys.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
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
    """Generate a random string of alphabetic characters.
    
    Args:
        length (int): The length of the string to generate.
    
    Returns:
        str: A string containing random alphabetical characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
