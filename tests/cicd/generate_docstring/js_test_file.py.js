
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
 * Compares two objects based on a specified key and provides a sorting order.
 * Returns -1 if the value of the specified key in the first object is less than that in the second, 
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param {string} keymap - The key used to extract values from the objects for comparison.
 * @param {Object} a - The first object for comparison.
 * @param {Object} b - The second object for comparison.
 * @returns {number} Returns -1, 0, or 1 based on the comparison of values.
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
 * Executes a query on an SQLite database and processes each row with a callback function.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The callback function to process each row of the query result set.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}