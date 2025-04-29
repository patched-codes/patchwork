# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on a SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the results of the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function and determines their order.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
    """Generates a random string of alphabets.
    
    Args:
        length (int): The desired length of the output string.
    
    Returns:
        str: A randomly generated string consisting of ASCII alphabets (both lower and uppercase) of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
