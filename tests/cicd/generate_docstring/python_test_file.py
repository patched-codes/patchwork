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
    """Executes a SQL query on the given database and returns the results.
    
    Args:
        db (sqlite3.Connection): The database connection object on which the query should be executed.
        query (str): The SQL query to be executed on the database.
    
    Returns:
        list: A list of tuples containing the rows returned by the query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compare two items using a key function.
    
    Args:
        key_map (Callable): A function that extracts a comparison key from each item.
        item1 (Any): The first item to compare.
        item2 (Any): The second item to compare.
    
    Returns:
        int: Returns -1 if the key from item1 is less than the key from item2,
             1 if the key from item1 is greater than the key from item2,
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
    """Generates a random string of alphabets of a specified length.
    
    Args:
        length int: The length of the random string to be generated.
    
    Returns:
        str: A string containing random uppercase and lowercase alphabets of the specified length.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
