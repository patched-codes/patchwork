
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
 * Compares two objects based on the value associated with a given key.
 * @param {String} keymap - The key name to be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {Number} - Returns -1 if the value of 'a' is less than the value of 'b',
 *                     1 if greater, or 0 if they are equal.
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
 * Executes a query on a given SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object to be queried.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - A function that will be called with each row of the result set.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}