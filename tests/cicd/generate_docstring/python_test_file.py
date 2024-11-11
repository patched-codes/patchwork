# fmt: off
def a_plus_b(a, b):
    """Add two numbers and return the result.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Execute a SQL query on a SQLite database and fetch all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched from the query result.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and returns an integer based on their comparison.
    
    Args:
        key_map function: A function that extracts a comparison key from each item.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2, 
             and 0 if both keys are equal.
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
    """Generates a random string consisting of alphabetic characters with a specified length.
    
    Args:
        length (int): The desired length of the generated string.
    
    Returns:
        str: A string composed of random alphabetic characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
