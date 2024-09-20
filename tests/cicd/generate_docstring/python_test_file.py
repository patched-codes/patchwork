def a_plus_b(a, b):
    """
    Computes the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the provided SQLite database and returns all fetched results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows fetched from the database after executing the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compare two items based on a key function and return a comparison result.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to be compared.
        item2 (any): The second item to be compared.
    
    Returns:
        int: -1 if item1 < item2, 1 if item1 > item2, 0 if they are equal based on the comparison key.
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
    Generates a random string of alphabetic characters of the specified length.
    
    Args:
        length (int): The number of characters in the generated string.
    
    Returns:
        str: A string of random alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
