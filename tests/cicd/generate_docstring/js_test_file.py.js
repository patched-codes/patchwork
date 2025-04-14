
/**
 * Computes the sum of two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the specified key and returns a numeric value
 * that indicates their relative order.
 * @param {string} keymap - The key used to compare the values in the objects.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the first object's key value is less than
 * the second, 1 if greater, and 0 if they are equal.
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
 * Executes a SQL query on a SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {function} callback - The callback function to be executed for each row of the result set.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}