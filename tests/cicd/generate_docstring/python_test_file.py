# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided SQLite database connection and retrieves all results.
    
    Args:
        db Connection: An SQLite database connection object.
        query str: The SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples representing the rows returned by the query, where each tuple is a row.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key mapping function.
    
    Args:
        key_map Callable: A function that extracts a comparison key from each item.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
    """Generate a random string of alphabets of the specified length.
    
    Args:
        length int: The length of the string to be generated.
    
    Returns:
        str: A string composed of random alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
