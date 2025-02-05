
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value at a specific key and determines their order.
 * Returns -1 if the value in the first object is smaller, 1 if it's larger, and 0 if they are equal.
 * 
 * @param {string}  keymap - The key based on which the comparison is made between the objects.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} -1 if `a` comes before `b`, 1 if `a` comes after `b`, or 0 if they are considered equal.
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
 * Executes an SQLite query on a database and applies a callback function to each row of the result.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {Function} callback - A callback function that is invoked once for each row returned by the query.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}