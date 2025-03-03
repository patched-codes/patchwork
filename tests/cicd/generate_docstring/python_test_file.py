# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of `a` and `b`.
    """
    
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on the provided SQLite database connection and fetches all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the results of the SQL query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a specified key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2, 
             or 0 if the keys are equal.
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
    """Generates a random string consisting of uppercase and lowercase alphabets.
    
    Args:
        length (int): The length of the random string to generate.
    
    Returns:
        str: A string consisting of random uppercase and lowercase alphabets with the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
