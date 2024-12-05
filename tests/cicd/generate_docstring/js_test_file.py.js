
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
 * Compares two objects based on the values associated with a specified key.
 * Returns -1 if the value for the key in object `a` is less than in object `b`, 
 * 1 if it's greater, or 0 if they are equal.
 * @param {string} keymap - The key used to access the values in objects `a` and `b` for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if value in `a` is less than in `b`, 1 if greater, or 0 if equal.
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
 * Executes a given SQL query on the provided SQLite database and applies a callback function to each row in the result set.
 * @param {Object} db - The SQLite database object on which the query is to be executed.
 * @param {string} query - The SQL query to execute.
 * @param {function} callback - The function to apply to each row of the result set.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}