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
    """Executes a SQL query on a SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list containing all rows of the query result, where each row is represented as a tuple.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key derived from each item using a given key function.
    
    Args:
        key_map (function): A function that takes an item and returns a key used for comparison.
        item1 (object): The first item to be compared.
        item2 (object): The second item to be compared.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if greater, and 0 if equal.
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
    """Generates a random string consisting of uppercase and lowercase alphabets of a specified length.
    
    Args:
        length (int): The length of the random alphabetic string to generate.
    
    Returns:
        str: A string made up of random alphabetical characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
