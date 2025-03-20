
/**
 * Adds two numbers and returns the result.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and returns a comparison result.
 * @param {string}  keymap - The key in the objects used for comparison.
 * @param {Object}  a - The first object to be compared.
 * @param {Object}  b - The second object to be compared.
 * @returns {number} Returns -1 if the value of `a[keymap]` is less than `b[keymap]`, 
 *                    1 if greater, and 0 if they are equal.
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
 * Executes an SQL query on the provided database connection and processes each result row using a callback function.
 * @param {Object} db - The database connection object used to execute the query.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - A function that will be called for each row in the result set, typically taking the row's data as input.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}