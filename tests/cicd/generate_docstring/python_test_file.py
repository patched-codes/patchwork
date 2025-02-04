# fmt: off
def a_plus_b(a, b):
    """Adds two numbers together.
    
    Args:
        a (numeric): The first number to be added.
        b (numeric): The second number to be added.
    
    Returns:
        numeric: The sum of the two numbers.
    """
    return a + b


def sqlite(db, query):
    """Executes a provided SQL query on a given SQLite database and returns the results.
    
    Args:
        db (sqlite3.Connection): The SQLite database connection object.
        query (str): The SQL query string to execute on the database.
    
    Returns:
        list: A list of tuples containing the rows of the query result.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on a key function.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             returns 1 if the key of item1 is greater than the key of item2, 
             or returns 0 if the keys are equal.
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
    """Generates a random string of alphabets of the specified length.
    
    Args:
        length (int): The length of the random alphabet string to be generated.
    
    Returns:
        str: A string consisting of randomly chosen alphabets with the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
