# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a SQLite database and retrieves all results.
    
    Args:
        db object: A SQLite database connection object used to execute the query.
        query str: A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items using a key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a value for comparison.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 
        or 0 if they are equal according to the key_map function.
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length int: The number of alphabets in the generated string.
    
    Returns:
        str: A string composed of randomly chosen alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
