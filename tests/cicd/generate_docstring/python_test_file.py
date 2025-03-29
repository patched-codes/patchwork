# fmt: off
def a_plus_b(a, b):
    """Computes the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The result of adding the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database and returns all the results.
    
    Args:
        db: sqlite3.Connection: The database connection object.
        query str: The SQL query to execute.
    
    Returns:
        list: A list containing all the rows resulting from the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a specified key mapping function.
    
    This function takes a mapping function and two items, applies the mapping
    to each item, and returns -1, 0, or 1 depending on whether the key of 
    the first item is less than, equal to, or greater than the key of the 
    second item.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2,
             0 if the keys are equal,
             1 if the key of item1 is greater than the key of item2.
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
    """Generate a random string of alphabets with the specified length.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A string consisting of randomly selected alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
