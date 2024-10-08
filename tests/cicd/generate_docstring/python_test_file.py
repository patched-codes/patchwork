def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers a and b.
    """
    
    return a + b


def sqlite(db, query):
    """Execute a SQL query on a SQLite database and return all fetched results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list containing all rows of the result set.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted by a provided key mapping function.
    
    Args:
        key_map (callable): A function that takes an item and returns a value used for comparison.
        item1 (any): The first item to compare, can be of any type that key_map can handle.
        item2 (any): The second item to compare, can be of any type that key_map can handle.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
    """Generates a random string of alphabets with a specified length.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
