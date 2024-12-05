
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on their values at the specified key.
 * 
 * @param {string} keymap - The key whose corresponding values in the objects should be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value in object 'a' is less than the value in object 'b', 
 *                    1 if the value in object 'a' is greater than the value in object 'b', 
 *                    and 0 if both values are equal.
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
 * Executes a SQL query on the given SQLite database and applies a callback function for each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The callback function to be called for each result row. The function receives parameters such as the error and the row object.
 * @returns {void} Does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}