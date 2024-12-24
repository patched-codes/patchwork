# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The result of adding the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection instance.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples representing the rows returned by the query. Each tuple contains the column values for a row.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a key mapping function.
    
    Args:
        key_map function: A function that takes an item as input and returns a value to compare.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
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
        length (int): The length of the random string to generate.
    
    Returns:
        str: A string consisting of random alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
