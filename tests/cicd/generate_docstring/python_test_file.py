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
    """Executes a SQL query on a given SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): An SQLite database connection object.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows resulting from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (object): The first item to compare.
        item2 (object): The second item to compare.
    
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
    """Generates a random string of alphabets of given length.
    
    Args:
        length (int): The number of alphabets to include in the generated string.
    
    Returns:
        str: A string of random alphabets with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
