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
    """
    Executes a SQL query on the provided SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list containing the rows returned by the executed query.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on their keys derived from a key-mapping function.
    
    Args:
        key_map (function): A function that extracts the key from an item for comparison.
        item1 (Any): The first item to be compared.
        item2 (Any): The second item to be compared.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2, 
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
    """Generates a random string of alphabets with a specified length.
    
    Args:
        length (int): The length of the string to be generated.
    
    Returns:
        str: A string containing random alphabets of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
