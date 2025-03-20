# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of `a` and `b`.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a provided SQLite database and returns all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a provided key mapping function.
    
    Args:
        key_map (callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal based on the key mapping.
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
    """Generate a random string consisting of alphabetic characters.
    
    Args:
        length int: The number of alphabetic characters to generate.
    
    Returns:
        str: A string composed of random alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
