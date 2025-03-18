
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns a numerical indication of their order.
 * @param {string} keymap - The key used to retrieve the values from objects 'a' and 'b' for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value from object 'a' is less than the value from object 'b', 
 * 1 if it is greater, or 0 if they are equal.
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
 * Executes an SQL query on the provided database and applies a callback function to each row in the result set.
 * @param {Object} db - An instance of a SQLite database connection.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - A callback function to be executed for each row of the query result; receives current row as an argument.
 * @returns {void} This function does not return any value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}