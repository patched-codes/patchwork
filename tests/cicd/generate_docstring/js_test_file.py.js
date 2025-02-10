
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
 * Compares two objects based on a specific key and returns a numerical value indicating their order.
 * This can be used for sorting purposes.
 * 
 * @param {string} keymap - The key in the objects 'a' and 'b' that will be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if 'a' is less than 'b', 1 if 'a' is greater than 'b', and 0 if they are equal based on the specified key.
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
 * Executes a SQLite query and processes the results with a callback function.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The callback function to be invoked for each row of the query result.
 * @returns {void} This function does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}