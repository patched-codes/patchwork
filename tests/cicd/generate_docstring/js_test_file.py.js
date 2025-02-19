
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
 * Compares two objects based on a specified key and returns an integer to indicate their order.
 * @param {string}  keymap - The key based on which the objects `a` and `b` should be compared.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1 if `a` is less than `b`, 1 if `a` is greater than `b`, and 0 if they are equal based on the specified key.
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
 * Executes a SQL query on an SQLite database and processes each resulting row using a callback function.
 * @param {Object} db - The SQLite database object on which to execute the query.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - A callback function to be invoked for each row in the result set. 
 *                              The callback is called with the arguments (err, row).
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}