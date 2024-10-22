def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Execute a SQL query on the given SQLite database connection and retrieve all results.
    
    Args:
        db (sqlite3.Connection): An SQLite database connection object.
        query (str): A SQL query string to be executed on the database.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a specified key mapping function.
    
    Args:
        key_map callable: A function that extracts a key from each item for comparison.
        item1 any: The first item to compare.
        item2 any: The second item to compare.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, 
             and 0 if they are equal based on the key extracted by key_map.
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
        length (int): The number of random alphabets to generate.
    
    Returns:
        str: A string comprised of random alphabets.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
