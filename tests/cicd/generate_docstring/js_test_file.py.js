
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of the specified key in each object.
 * @param {string}  keymap - The key used to access values in the objects for comparison.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a[keymap]` is less than `b[keymap]`, 
 * 1 if it's greater, and 0 if they are equal.
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
 * Executes a specified SQL query on a given database and processes each row of the result with a callback function.
 * @param {object}  db - The SQLite database object on which the query is to be executed.
 * @param {string}  query - The SQL query string to be executed on the database.
 * @param {function} callback - A function that is called for each row of the result set. 
 * @returns {void}
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}