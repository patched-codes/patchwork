# fmt: off
def a_plus_b(a, b):
    """Returns the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on the given SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): An open SQLite database connection object.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list containing all rows of the result set after executing the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and determines their order.
    
    Args:
        key_map (function): A function that takes an item and returns a value by which the item is compared.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length (int): The length of the random string to generate.
    
    Returns:
        str: A string containing random alphabets of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
