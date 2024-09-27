def a_plus_b(a, b):
    """
    Computes the sum of two numbers.
    
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.
    
    Returns:
        int, float: The sum of the two given numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on an SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object to execute the query on.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that extracts a key from each item for comparison.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: -1 if the key of `item1` is less than the key of `item2`, 
             1 if the key of `item1` is greater than the key of `item2`, 
             0 if the keys are equal.
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
        length int: The desired length of the random alphabet string.
    
    Returns:
        str: A string of random alphabets of the given length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
