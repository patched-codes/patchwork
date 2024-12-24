
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of `a` and `b`.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a key value as specified by the keymap.
 * Returns -1 if object 'a' has a lesser value for the keymap than object 'b',
 * 1 if 'a' has a greater value, and 0 if they are equal.
 * 
 * @param {string} keymap - The key in the objects 'a' and 'b' used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1, 0, or 1 based on the comparison of the objects.
 */
const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

/**
 * Executes a SQL query on a given SQLite database, calling a callback function for each row of the result.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {Function} callback - The function to be executed for each row that is retrieved by the SQL query.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}