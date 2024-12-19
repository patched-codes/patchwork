# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQL query on the provided SQLite database connection and fetches all results.
    
    Args:
        db sqlite3.Connection: The SQLite database connection object.
        query str: The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched from the database as the result of the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key function and returns an integer based on their comparison.
    
    Args:
        key_map function: A function that extracts a comparison key from each element.
        item1 object: The first item to be compared.
        item2 object: The second item to be compared.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2,
             1 if the key of item1 is greater than the key of item2,
             0 if the keys are equal.
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
        str: A string composed of randomly selected alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
