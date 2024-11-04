# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.
    
    Returns:
        int, float: The sum of the two numbers a and b.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the provided database connection and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute on the database.
    
    Returns:
        list: A list of tuples containing the rows retrieved from the query execution.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that extracts a key from an item for comparison.
        item1 (object): The first item to be compared.
        item2 (object): The second item to be compared.
    
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
    """Generate a random string of alphabets of the specified length.
    
    Args:
        length int: The number of random alphabets to generate.
    
    Returns:
        str: A string composed of random alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
