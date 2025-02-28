# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes an SQL query on a given SQLite database connection and retrieves all results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows fetched from the database after the query execution.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a given key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2,
             1 if the key of item1 is greater than the key of item2,
             and 0 if both keys are equal.
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
        length (int): The desired length of the random alphabet string.
    
    Returns:
        str: A string composed of random alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
