def a_plus_b(a, b):
    """Calculates the sum of two numbers.
    
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of the two given numbers.
    """
    
    return a + b


def sqlite(db, query):
    """Execute a query on the provided SQLite database connection and fetch all results.
    
    Args:
        db sqlite3.Connection: The SQLite database connection object.
        query str: The SQL query to be executed on the database.
    
    Returns:
        list: A list containing the results of the executed query, where each result is a tuple.
    """
    
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    """Compares two items based on their transformed values using a key-mapping function.
    
    Args:
        key_map function: A function that extracts a comparison key from each item.
        item1 any: The first item to be compared.
        item2 any: The second item to be compared.
    
    Returns:
        int: Returns -1 if the key of item1 is less than the key of item2, 
             1 if the key of item1 is greater than the key of item2,
             and 0 if both keys are equal.
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
    """Generate a random string of alphabetic characters.
    
    Args:
        length int: The length of the string to be generated.
    
    Returns:
        str: A string of randomly selected alphabetic characters of the specified length.
    """
    
    return ''.join(random.choices(string.ascii_letters, k=length))
