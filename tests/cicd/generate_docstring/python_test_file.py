# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided SQLite database connection and fetches all results.
    
    Args:
        db: A SQLite database connection object.
        query str: The SQL query to be executed on the database.
    
    Returns:
        list: A list containing all rows of the result set from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a key mapping function.
    
    Args:
        key_map (Callable): A function that maps an item to a key for comparison.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if greater, and 0 if they are equal.
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
    """Generate a random string of alphabetic characters.
    
    Args:
        length (int): The length of the string to generate.
    
    Returns:
        str: A string consisting of randomly chosen alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
