def a_plus_b(a, b):
    """
    Adds two numbers.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """
    Executes a SQL query on a given SQLite database and retrieves all results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples representing the rows fetched from the query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items based on a key function.
    
    Args:
        key_map (function): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if their keys are equal.
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
    Generates a random string of alphabets with the specified length.
    
    Args:
        length int: The length of the random string to be generated.
    
    Returns:
        str: A random string consisting of uppercase and lowercase alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))