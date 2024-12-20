# fmt: off
def a_plus_b(a, b):
    """Returns the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the parameters a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes an SQL query on a given SQLite database connection and returns all rows fetched.
    
    Args:
        db sqlite3.Connection: The SQLite database connection object to be used to execute the query.
        query str: The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples representing the rows fetched by executing the SQL query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted by a given function and returns an integer based on their order.
    
    Args:
        key_map function: A function that takes an item and returns its corresponding key for comparison.
        item1 Any: The first item to compare.
        item2 Any: The second item to compare.
    
    Returns:
        int: Returns -1 if the first item is less than the second item, 1 if the first item is greater, and 0 if they are equal.
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
    """Generate a random string of alphabets of specified length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
