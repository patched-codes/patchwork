
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
 * Compares two objects based on the value of a given key within a keymap.
 * Returns -1 if a's key value is less than b's key value, 1 if greater, and 0 if equal.
 *
 * @param {string} keymap - The key in the objects 'a' and 'b' to compare.
 * @param {Object} a - The first object for comparison.
 * @param {Object} b - The second object for comparison.
 * @returns {number} Returns -1, 1, or 0 based on the comparison of key values between 'a' and 'b'.
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
 * Executes a SQL query on a SQLite database and invokes a callback function for each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The function to be called for each row in the result set.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}