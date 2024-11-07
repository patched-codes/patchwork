# fmt: off
def a_plus_b(a, b):
    """Adds two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database connection and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a mapping key function.
    
    Args:
        key_map (function): A function that takes an item and returns a key for comparison.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             returns 1 if the key of item1 is greater than the key of item2, 
             returns 0 if both keys are equal.
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
    """Generate a random string of alphabets with a specified length.
    
    Args:
        length (int): The length of the random alphabet string to be generated.
    
    Returns:
        str: A string consisting of randomly chosen alphabets of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
