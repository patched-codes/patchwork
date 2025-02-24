
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and determines their order.
 * This function is useful for sorting arrays of objects.
 *
 * @param {string} keymap - The key in the objects to compare their values.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of the specified key in 'a' is less than in 'b',
 * returns 1 if it is greater, or returns 0 if they are equal.
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
 * Executes a SQL query on a SQLite database and processes each row with a callback function.
 * @param {Object}  db - The SQLite database object to operate on.
 * @param {string}  query - The SQL query to be executed on the database.
 * @param {Function} callback - A function to be executed on each row of the query result.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}