# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on a SQLite database and fetch all results.
    
    Args:
        db (sqlite3.Connection): The database connection object.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the rows retrieved by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items using a key function.
    
    Args:
        key_map (function): A function that takes an item and returns a value to be compared.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
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
    """Generate a random string of alphabets of a specified length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A string consisting of randomly selected alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
