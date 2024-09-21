def a_plus_b(a, b):
    """
    Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided database connection and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key generated by the provided key_map function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if key_map(item1) < key_map(item2),
             1 if key_map(item1) > key_map(item2),
             0 if key_map(item1) == key_map(item2).
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
    """Generate a random string of alphabetic characters of specified length.
    
    Args:
        length (int): The length of the generated string.
    
    Returns:
        str: A string consisting of random alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
