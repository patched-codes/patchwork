
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */

function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and determines their order.
 * @param {string}  keymap - The key used for comparison in objects a and b.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} -1 if a[key] is less than b[key], 1 if a[key] is greater than b[key], 0 if they are equal.
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
 * Executes a SQL query on the provided database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object on which the query is to be run.
 * @param {string} query - The SQL query string to execute.
 * @param {function} callback - The callback function to be invoked for each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}