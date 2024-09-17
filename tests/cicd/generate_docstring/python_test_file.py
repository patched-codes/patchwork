def a_plus_b(a, b):
    """
    Computes the sum of two numbers.
    
    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.
    
    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on a given SQLite database and fetches the result.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the fetched rows from the query result.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key function.
    
    Args:
        key_map (function): A function that takes an item and returns a key for comparison.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if they are equal.
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
    Generate a random string of alphabets of the specified length.
    
    Args:
        length int: The length of the random string to generate.
    
    Returns:
        str: A randomly generated string containing alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))