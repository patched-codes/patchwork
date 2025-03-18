# fmt: off
def a_plus_b(a, b):
    """
    Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two input numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a SQL query on the provided SQLite database and returns all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list containing all rows of the query result from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key for item1 is less than the key for item2, 
             returns 1 if the key for item1 is greater than the key for item2,
             and returns 0 if both keys are equal.
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
    """Generate a random sequence of alphabetic characters.
    
    Args:
        length (int): The number of random alphabetic characters to generate.
    
    Returns:
        str: A string consisting of randomly selected alphabetic characters of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
