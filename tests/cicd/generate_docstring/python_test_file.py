# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a specified SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples, each tuple representing a row retrieved by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a provided key mapping function.
    
    Args:
        key_map function: A function that extracts a comparison key from each item.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: -1 if the key for item1 is less than the key for item2, 
             1 if the key for item1 is greater than the key for item2,
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length (int): The number of characters in the generated string.
    
    Returns:
        str: A randomly generated string consisting of uppercase and lowercase alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
