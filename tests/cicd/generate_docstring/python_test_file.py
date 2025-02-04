# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes an SQL query on a given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function and returns an integer indicating their order.
    
    Args:
        key_map function: A function that extracts a comparison key from each element in the comparison.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, or 0 if they are equal.
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length (int): The length of the random string to generate.
    
    Returns:
        str: A string consisting of randomly selected alphabetical characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
