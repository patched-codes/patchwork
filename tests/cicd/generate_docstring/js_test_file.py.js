
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of numbers a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns a comparison result.
 * @param {string} keymap - The key in the objects that is used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of the key in object 'a' is less than in object 'b', 
 *                     1 if the value is greater, and 0 if they are equal.
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
 * Executes a SQL query on a SQLite database and applies a callback to each row of the result.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The callback function to be applied to each row in the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}