
/**
 * Adds two numbers together and returns the sum.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key.
 * @param {string} keymap - The key name used to access the values in each object for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of `a` is less than the value of `b`, returns 1 if the value of `a` is greater than the value of `b`, and returns 0 if both values are equal.
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
 * Executes a query on a given SQLite database and applies a callback function to each row.
 * @param {Object} db - The SQLite database instance to perform the query on.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The function to be called for each row of the query result. The callback receives the current row as an argument.
 * @returns {void} No return value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}