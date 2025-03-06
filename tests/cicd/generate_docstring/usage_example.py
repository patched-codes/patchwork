import sqlite3
import random
import string
from your_module import a_plus_b, sqlite, compare, random_alphabets

# Example 1: Using a_plus_b function
result = a_plus_b(5, 3)
print(f"5 + 3 = {result}")  # Outputs: 5 + 3 = 8

# Example 2: Using sqlite function
# Establish an in-memory SQLite database and populate a sample table
db = sqlite3.connect(':memory:')
with db:
    db.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("INSERT INTO test (name) VALUES ('Alice'), ('Bob')")

# Query the database
query = "SELECT * FROM test"
results = sqlite(db, query)
print("SQLite query results:", results)  # Outputs: SQLite query results: [(1, 'Alice'), (2, 'Bob')]

# Example 3: Using compare function
item1 = {'value': 10}
item2 = {'value': 15}
comparison = compare(lambda x: x['value'], item1, item2)
comparison_text = ["less than", "equal to", "greater than"][comparison + 1]
print(f"Item1 is {comparison_text} Item2")  # Outputs: Item1 is less than Item2

# Example 4: Using random_alphabets function
random_string = random_alphabets(8)
print(f"Random string: {random_string}")  # Outputs a random string of 8 alphabets
