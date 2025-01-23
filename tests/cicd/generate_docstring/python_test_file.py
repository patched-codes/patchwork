# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the specified SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): An open connection to the SQLite database.
        query (str): The SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples, with each tuple representing a row from the query result set.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal, according to the keys obtained using key_map.
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
    """Generate a random string of alphabets.
    
    Args:
        length int: The length of the resulting random alphabet string.
    
    Returns:
        str: A string consisting of randomly chosen alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
