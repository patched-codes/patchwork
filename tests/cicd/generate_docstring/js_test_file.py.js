
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
 * Compares two objects based on a specified key and determines their order.
 * The comparison is made using the values associated with the provided key in each object.
 * 
 * @param {string} keymap - The key to use for comparing values between object `a` and object `b`.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of object `a` is less than the value of object `b`,
 *                   1 if the value of object `a` is greater than the value of object `b`,
 *                   or 0 if they are equal.
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
 * Executes a SQLite query on the provided database and applies a callback function to each resulting row.
 * @param {Object} db - The SQLite database object on which the query is executed.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The callback function that processes each row of the query result.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}