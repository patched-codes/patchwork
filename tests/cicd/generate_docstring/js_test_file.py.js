
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */

function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on a SQLite database and processes each result row with a callback function.
 * @param {Object}  db - The SQLite database object.
 * @param {string}  query - The SQL query to be executed.
 * @param {Function}  callback - The callback function to process each result row. It receives the row data as a parameter.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the values of a specified key.
 * @param {string} keymap - The key whose corresponding values in objects `a` and `b` will be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of `a[keymap]` is less than `b[keymap]`, 
 *                     1 if the value of `a[keymap]` is greater than `b[keymap]`, 
 *                     and 0 if they are equal.
 */
const compare= function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}