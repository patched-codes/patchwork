def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the results of the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compare two items based on a key mapping function.
    
    Args:
        key_map function: A function that extracts a comparison key from each item.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, 0 if item1 == item2.
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
    Generates a random string of alphabets of a specified length.
    
    Args:
        length int: The length of the resulting random string.
    
    Returns:
        str: A string composed of randomly chosen alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))