
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key.
 * Returns -1 if the value of the specified key in 'a' is less than in 'b',
 * 1 if it is greater, and 0 if they are equal.
 *
 * @param {string} keymap - The key used to compare the two objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1, 0, or 1 based on the comparison of the specified key values.
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
 * Executes a query on a given SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object where the query will be executed.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - The function to be called for each row of the query result.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}