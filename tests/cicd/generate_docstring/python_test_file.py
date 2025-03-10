# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be summed.
        b (int or float): The second number to be summed.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on a SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The database connection object to execute the query on.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing all rows returned by the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on their keys obtained through a transformation function.
    
    Args:
        key_map (function): A function that takes an item as input and returns a key for comparison.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if greater, and 0 if they are equal.
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
    """Generates a random string of alphabets of specified length.
    
    Args:
        length int: The length of the random alphabetic string to be generated.
    
    Returns:
        str: A string consisting of randomly selected alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
