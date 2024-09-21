
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQL query on the provided SQLite database and processes each row with a callback function.
 * @param {object} db - SQLite database object.
 * @param {string} query - SQL query string to execute.
 * @param {function} callback - Callback function to process each row returned by the query.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of the key in object `a` is less than the value in object `b`, 
 *                      1 if the value of the key in object `a` is greater than the value in object `b`, 
 *                      and 0 if they are equal.
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