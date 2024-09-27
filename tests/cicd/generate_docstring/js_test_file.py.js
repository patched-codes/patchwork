
/**
 * Adds two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes an SQLite query on a given database and processes each row of the result using a callback function.
 * @param {Object}  db - The SQLite database connection object.
 * @param {string}  query - The SQL query string to be executed.
 * @param {Function}  callback - The function to be called for each row in the result set. This function takes two parameters: error and row.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key on which to compare the two objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of key in object `a` is less than in object `b`,
 *                    1 if the value of key in object `a` is greater than in object `b`,
 *                    and 0 if they are equal.
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