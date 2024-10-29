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
    """Executes a SQL query on a given SQLite database connection and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples representing the rows retrieved by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function.
    
    Args:
        key_map (function): A function that extracts the key from an item for comparison.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if greater, or 0 if they are equal.
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
        length (int): The length of the random alphabet string to be generated.
    
    Returns:
        str: A string consisting of randomly selected alphabets of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
