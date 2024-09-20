
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a serialized query on the SQLite database and processes each row with the provided callback function.
 * @param {Object} db - The SQLite database instance.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The callback function to be called for each row of the query result.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and returns a numerical value indicating their relative order.
 * @param {string} keymap - The key used for comparison within the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a[keymap]` is less than `b[keymap]`, 
 *                   1 if the value of `a[keymap]` is greater than `b[keymap]`, 
 *                   and 0 if they are equal.
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