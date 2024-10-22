
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and determines their order.
 * @param {string} keymap - The key in the objects to compare.
 * @param {Object} a - The first object for comparison.
 * @param {Object} b - The second object for comparison.
 * @returns {number} Returns -1 if the value of the key in object a is less than the value of the key in object b, 
 *          1 if it's greater, or 0 if they are equal.
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
 * Executes a given SQL query on a SQLite database and applies a callback function to each row of the result set.
 * @param {Object} db - The SQLite database object to run the query against.
 * @param {String} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be executed for each row result. The function receives the row data as its argument.
 * @returns {void} This function does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}