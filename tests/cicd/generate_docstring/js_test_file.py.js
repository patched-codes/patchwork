
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key used to extract values from the objects for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater, and 0 if they are equal.
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
 * Executes a given SQLite query on the specified database and applies a callback function for each row in the result set.
 * @param {Object} db - The SQLite database instance on which the query will be executed.
 * @param {string} query - SQL query string to be executed.
 * @param {Function} callback - Callback function that will be called for each row resulting from the query. Receives the row as an argument.
 * @returns {void} No value is returned from this function.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}