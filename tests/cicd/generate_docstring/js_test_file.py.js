
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key and returns an integer 
 * indicating their relative order.
 * @param {string} keymap - The key in the objects `a` and `b` used for comparison.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if `a[keymap]` is less than `b[keymap]`, 
 *                   1 if `a[keymap]` is greater than `b[keymap]`, 
 *                   and 0 if both are equal.
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
 * Executes a provided SQL query on a SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object to execute the query on.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - The callback function to apply to each row in the query result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}