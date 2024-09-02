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
    Executes a SQL query on the given SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched by the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that takes an item and returns a value to be used for comparison.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than item2, 0 if they are equal.
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
    Generates a random string of alphabetic characters of a given length.
    
    Args:
        length (int): The length of the generated random string.
    
    Returns:
        str: A string consisting of randomly chosen alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))