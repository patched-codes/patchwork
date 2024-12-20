
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
 * Compares two objects based on the values of a specified key.
 * @param {string}  keymap - The key in the objects to be used for comparison.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1 if the value at the specified key in object `a` is less than that in object `b`,
 *                      1 if greater, and 0 if they are equal.
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
 * Executes a SQL query on a given SQLite database and applies a callback function to each row of the result set.
 * @param {object} db - The SQLite database connection object on which the query is executed.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - A callback function that is applied to each row in the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}