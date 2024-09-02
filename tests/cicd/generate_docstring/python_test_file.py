def a_plus_b(a, b):
    """
    Adds two numbers together.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of a and b.
    """    return a + b


def sqlite(db, query):
    """
    Executes an SQL query on a given SQLite database and returns all the results.
    
    Args:
        db (sqlite3.Connection): An open SQLite database connection.
        query (str): The SQL query to execute on the database.
    
    Returns:
        list: A list of tuples containing all the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key mapping function.
    
    Args:
        key_map (callable): A function that extracts a comparable key from an item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, 0 if they are equal.
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
    Generates a random string of alphabets.
    
    Args:
        length (int): The desired length of the random string.
    
    Returns:
        str: A random string consisting of ASCII letters with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))