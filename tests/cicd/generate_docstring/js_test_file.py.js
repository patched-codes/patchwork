
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
 * Compares two objects based on a specific key and returns an integer to indicate their order.
 * @param {string} keymap - The key on which the objects are compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a' is less than 'b', 1 if greater, and 0 if they are equal.
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
 * Executes a SQL query on the provided SQLite database and applies a callback function to each result.
 * The database operations are performed in a serialized manner.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The function that is called for each row in the result set. 
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}