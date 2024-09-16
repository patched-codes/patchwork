def a_plus_b(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on the provided SQLite database connection and returns the fetched results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the fetched rows from the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the key for item1 is less than the key for item2, 
             1 if the key for item1 is greater than the key for item2,
             and 0 if the keys are equal.
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
        length int: The length of the random alphabet string to generate.
    
    Returns:
        str: A randomly generated string of alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))