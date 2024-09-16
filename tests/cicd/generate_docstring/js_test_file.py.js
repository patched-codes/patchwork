
/**
 * Adds two numbers together.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */

function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given query on the provided SQLite database and applies a callback to each result row.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query string to execute.
 * @param {function} callback - The callback function to apply to each result row.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a given key.
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of the key in 'a' is less than in 'b', 1 if greater, and 0 if they are equal.
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