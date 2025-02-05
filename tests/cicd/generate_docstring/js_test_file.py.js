
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and returns a comparison result.
 * @param {string} keymap - The key which the comparison is based on.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value in object 'a' is less than in object 'b', 1 if greater, and 0 if equal.
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
 * Executes a SQL query on the given SQLite database connection and applies the callback function to each row in the result set.
 * @param {Object}  db - The SQLite database connection object.
 * @param {string}  query - The SQL query string to be executed.
 * @param {Function}  callback - The callback function that will be invoked for each row in the result set, receiving the current row as its argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}