
/**
 * Returns the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a provided SQL query on a SQLite database and applies a callback function to each result row.
 * @param {object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The callback function to be applied to each result row from the query.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the values of a specified key.
 * @param {string} keymap - The key used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if `a[keymap]` is less than `b[keymap]`, 1 if greater, and 0 if they are equal.
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