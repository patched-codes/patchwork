
/**
 * Adds two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns a sorting order indicator.
 * @param {string}  keymap - The key in the objects 'a' and 'b' used for comparison.
 * @param {Object}  a - The first object to be compared.
 * @param {Object}  b - The second object to be compared.
 * @returns {number} A negative number if 'a' is less than 'b', a positive number if 'a' is greater than 'b', and zero if they are equal.
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
 * Executes a SQLite query using the provided database connection and calls a callback for each row retrieved.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to execute.
 * @param {Function} callback - The function to call for each row retrieved by the query. It receives (err, row) as arguments.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}