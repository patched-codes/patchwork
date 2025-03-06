# fmt: off
def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Executes an SQL query on a given SQLite database and fetches all results.
    
    Args:
        db (sqlite3.Connection): The database connection object.
        query (str): The SQL query string to be executed.
    
    Returns:
        list: A list of tuples containing the results of the executed query.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key mapping function.
    
    Args:
        key_map function: A function that takes an item as an argument and returns a comparable value.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal according to the key_map function.
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
    """Generate a random string of alphabets.
    
    Args:
        length int: The length of the string to be generated.
    
    Returns:
        str: A string containing randomly selected alphabetic characters.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
