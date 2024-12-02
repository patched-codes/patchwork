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
    """Executes a given SQL query on a SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): A connection object that represents the SQLite database.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples where each tuple represents a row resulting from the query execution.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a specified key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparison key from an item.
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
        length (int): The number of random alphabets to generate.
    
    Returns:
        str: A string containing random alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
