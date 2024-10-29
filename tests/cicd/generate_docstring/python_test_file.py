# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes a given SQL query on the specified SQLite database and retrieves all resulting records.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list containing all rows of the query result, with each row represented as a tuple.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a specified key mapping function.
    
    Args:
        key_map function: A function that takes an item and returns a comparable key.
        item1 object: The first item to compare.
        item2 object: The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2, 
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
    """Generates a random string of alphabets with the specified length.
    
    Args:
        length (int): The length of the random string to be generated.
    
    Returns:
        str: A random string composed of upper and lowercase alphabets.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
