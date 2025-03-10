# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a provided SQLite database connection and retrieves all results.
    
    Args:
        db (Connection): A SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list containing tuples of the results retrieved from the SQL query execution.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and returns an integer based on their comparison.
    
    Args:
        key_map function: A function that extracts a comparison key from each item.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
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
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A string consisting of randomly selected alphabets of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
