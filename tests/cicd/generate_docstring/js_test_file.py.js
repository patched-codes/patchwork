
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
 * Compares two objects based on a specified key and determines their ordering.
 * @param {string} keymap - The key by which the objects should be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} A negative number if the first object is less than the second,
 *                   a positive number if the first object is greater than the second,
 *                   or zero if they are equal based on the specified key.
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
 * Executes a provided SQL query on a given SQLite database and applies a callback function to each row of the result.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - The callback function to be applied to each row of the query result.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}