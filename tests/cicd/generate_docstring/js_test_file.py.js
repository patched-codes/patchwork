
/**
 * Adds two numbers together
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects `a` and `b` based on the values of a specified key `keymap`.
 * Returns -1 if `a[keymap]` is less than `b[keymap]`, 1 if `a[keymap]` is greater than `b[keymap]`, and 0 if they are equal.
 * 
 * @param {string} keymap - The key used to compare values in objects `a` and `b`.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1, 0, or 1 based on the comparison.
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
 * Executes a SQL query on a SQLite database and processes each result with a callback function.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - The function to execute for each row in the result set. 
 *                             The callback is invoked with arguments: (error, row).
 * @returns {void}
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}