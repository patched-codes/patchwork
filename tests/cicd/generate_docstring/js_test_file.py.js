
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects `a` and `b` based on the values of their properties
 * specified by the `keymap`. The function returns -1 if `a`'s property is less
 * than `b`'s property, 1 if `a`'s property is greater than `b`'s property, and
 * 0 if they are equal.
 * 
 * @param {string} keymap - The property name by which the comparison is made.
 * @param {Object} a - The first object containing the property to compare.
 * @param {Object} b - The second object containing the property to compare.
 * @returns {number} Returns -1, 0, or 1 depending on the comparison of `a` and `b`.
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
 * Executes a provided SQL query on a given SQLite database and applies a callback function to each row of result.
 * @param {object} db - The SQLite database connection object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The callback function to be called with each row of the result. Function signature: function(row) {}
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}