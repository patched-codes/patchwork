
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
 * Compares two objects based on a specific property defined by the keymap and returns an integer indicating their order.
 * @param {string} keymap - The key to be used in both objects for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if object 'a' is less than object 'b', 1 if object 'a' is greater than object 'b', or 0 if they are equal.
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
 * Executes a provided SQL query on a serialized SQLite database and processes each row of the result set using a callback function.
 * @param {Object} db - An SQLite database object on which the query is to be executed.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {Function} callback - A function that gets called for each resulting row. The callback function receives the row object as its argument.
 * @returns {void} Does not return a result.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}