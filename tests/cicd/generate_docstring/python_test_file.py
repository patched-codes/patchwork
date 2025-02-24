# fmt: off
def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.
    
    Returns:
        int, float: The sum of the two input numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on a SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): A SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list containing the rows returned from the SQL query, with each row being a tuple.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a key mapping function and returns an integer based on their comparison.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 1 if it's greater, 
        and 0 if they are equal.
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
    """Generate a random string of alphabets of a given length.
    
    Args:
        length (int): The length of the random alphabet string to generate.
    
    Returns:
        str: A string consisting of random alphabetical characters with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
