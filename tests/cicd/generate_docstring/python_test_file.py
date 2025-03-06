# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided SQLite database connection and retrieves all results.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database where the query will be executed.
        query (str): A SQL query string to execute on the connected database.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key function and returns an integer indicating their order.
    
    Args:
        key_map (function): A function that takes an item and returns a key to compare.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the first item is less than the second, 1 if the first item is greater than the second, and 0 if they are equal.
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
    Generates a random string of alphabets of specified length.
    
    Args:
        length (int): The length of the desired random alphabetic string.
    
    Returns:
        str: A string consisting of random alphabetic characters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
