
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the given SQL query on the provided database and processes each row using the callback function.
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The function to be called for each row in the result set.
 * @returns {void} Executes the query and processes the rows, does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and determines their order.
 * @param {string} keymap - The key to use for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], and 0 if they are equal.
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