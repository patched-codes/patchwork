# fmt: off
def a_plus_b(a, b):
    """Add two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a SQL query on a given SQLite database connection and fetches all results.
    
    Args:
        db (sqlite3.Connection): A connection object to the SQLite database.
        query (str): The SQL query to be executed.
    
    Returns:
        list: A list of tuples containing the fetched results from the database.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items using a key map function and returns an integer 
    indicating their ordering.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from 
                            each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: -1 if item1 is less than item2, 1 if item1 is greater than 
             item2, and 0 if they are equal.
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
    """Generate a random string of alphabets of a specified length.
    
    Args:
        length (int): The number of random alphabetic characters to generate.
    
    Returns:
        str: A string containing randomly selected alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
