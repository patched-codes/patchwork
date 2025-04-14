# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the input numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on an SQLite database and retrieves the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted by a key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater 
        than the key of item2, or 0 if the keys are equal.
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
        str: A string of randomly selected alphabets with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
