# fmt: off
def a_plus_b(a, b):
    """Calculate the sum of two values.
    
    Args:
        a (int, float): The first value to be added.
        b (int, float): The second value to be added.
    
    Returns:
        int, float: The sum of the input values a and b.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on the given database connection and return all fetched results.
    
    Args:
        db (sqlite3.Connection): The database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows fetched from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key function and returns an integer indicating their order.
    
    Args:
        key_map (callable): A function that takes an item and returns a value to compare.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the value of item1 is less than the value of item2, 1 if the value of item1 is greater than the value of item2, or 0 if they are equal.
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
        length (int): The length of the random string to generate.
    
    Returns:
        str: A string consisting of randomly selected alphabetic characters, both uppercase and lowercase.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
