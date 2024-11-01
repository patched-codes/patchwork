
/**
 * Computes the sum of two numbers.
 * @param {number}  a - The first number.
 * @param {number}  b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specific key and returns a comparison value.
 * @param {string} keymap - The key of the objects that should be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if value in object 'a' is less than value in 'b', 1 if greater, and 0 if equal.
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
 * Executes a query on a SQLite database and applies a callback to each result row.
 * @param {object} db - The SQLite database instance to run the query on.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {function} callback - The function to be called on each row of the result set. It receives the current row as an argument.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}