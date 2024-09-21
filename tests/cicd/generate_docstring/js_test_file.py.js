
/**
 * Computes the sum of two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on the provided SQLite database and processes each row of result set using a callback function.
 * 
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The callback function to be executed for each row of the result set. 
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and returns a comparison value.
 *
 * @param {string} keymap - The key based on which the comparison is performed.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of keymap in object 'a' is less than in object 'b',
 *                     1 if the value of keymap in object 'a' is greater than in object 'b', 
 *                     and 0 if the values are equal.
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