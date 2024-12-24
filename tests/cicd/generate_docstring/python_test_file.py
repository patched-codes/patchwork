# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key extracted from each item using a given key mapping function.
    
    Args:
        key_map function: A function that extracts a key from the given item.
        item1 any: The first item to compare, can be of any data type that key_map handles.
        item2 any: The second item to compare, can be of any data type that key_map handles.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if both keys are equal.
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
        length (int): The number of characters in the generated string.
    
    Returns:
        str: A string consisting of random alphabetical characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
