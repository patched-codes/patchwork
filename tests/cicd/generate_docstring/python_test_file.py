# fmt: off
def a_plus_b(a, b):
    """Computes the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and retrieves all results.
    
    Args:
        db (Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a specified key mapping function and determines their relative order.
    
    Args:
        key_map function: A function that maps an item to a comparable key.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2,
             1 if the key of item1 is greater than the key of item2,
             or 0 if both keys are equal.
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
    """Generates a random string of alphabets of a specified length.
    
    Args:
        length int: The length of the random string to be generated.
    
    Returns:
        str: A string consisting of randomly chosen alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
