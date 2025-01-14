# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The result of adding the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a provided database connection and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items using a custom key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal based on the key_map function.
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
    """Generates a random string of alphabets of a specified length.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A string consisting of random alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
