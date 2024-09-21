def a_plus_b(a, b):
    """
    Computes the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function.
    
    Args:
        key_map (callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
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
    Generate a random string of alphabets.
    
    Args:
        length int: The length of the generated string.
    
    Returns:
        str: A random string of alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
