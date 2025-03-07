# fmt: off
def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on a provided SQLite database connection and retrieves all the resulting records.
    
    Args:
        db: Database connection object: The SQLite database connection.
        query str: The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples, where each tuple represents a row resulting from the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on their keys obtained through a mapping function.
    
    Args:
        key_map (function): A function that extracts keys from the given items for comparison.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2,
             1 if the key of item1 is greater than the key of item2,
             or 0 if both keys are equal.
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
    """Generate a random string of alphabets with specified length.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A string containing randomly selected alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
