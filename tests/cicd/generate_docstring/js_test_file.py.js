
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
 * Executes a SQL query on a given SQLite database and handles the result through a callback function.
 * @param {object} db - The SQLite database object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The callback function to handle the result of each row retrieved by the query.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key.
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of the key in the first object is less than the second object's value.
 *                     Returns 1 if the value of the key in the first object is greater than the second object's value.
 *                     Returns 0 if both values are equal.
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