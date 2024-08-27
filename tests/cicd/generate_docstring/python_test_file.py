def a_plus_b(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (number): The first number.
        b (number): The second number.
    
    Returns:
        number: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the given SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the rows fetched by the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a specified key mapping function.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if the keys are equal.
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
    Generate a random string of alphabets with a given length.
    
    Args:
        length int: The number of random alphabetic characters to generate.
    
    Returns:
        str: A string composed of random alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))