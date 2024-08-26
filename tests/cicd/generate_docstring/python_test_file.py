def a_plus_b(a, b):
    return a + b


def sqlite(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def compare(key_map, item1, item2):
    if key_map(item1) < key_map(item2):
        return -1
    elif key_map(item1) > key_map(item2):
        return 1
    else:
        return 0

def random(
        length: int
):
    return ''.join(random.choices(string.ascii_letters, k=length))