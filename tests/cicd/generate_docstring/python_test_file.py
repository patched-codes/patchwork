def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a given SQL query on the provided SQLite database connection.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of rows returned by the query.
    
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a provided key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a value to be used for comparison.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the value from key_map(item1) is less than key_map(item2),
             1 if it is greater, and 0 if they are equal.
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
    """
    Generate a random string of alphabets with a specified length.
    
    Args:
        length (int): The number of alphabets in the generated string.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
