# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the rows returned by the query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """
    Compares two items using a specified key function and returns their ordering.
    
    Args:
        key_map (function): A function that extracts a comparison key from each element in `item1` and `item2`.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if `item1` is less than `item2`, 1 if `item1` is greater than `item2`, and 0 if both are equal.
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
    """Generates a random string consisting of alphabetical characters.
    
    Args:
        length int: The length of the random string to be generated.
    
    Returns:
        str: A string consisting of randomly chosen alphabetical characters (both uppercase and lowercase).
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
