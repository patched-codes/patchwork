
/**
 * Returns the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns a numerical value indicating their order.
 * @param {string}  keymap - A string representing the key to compare the objects by.
 * @param {object}  a - The first object to compare.
 * @param {object}  b - The second object to compare.
 * @returns {number} A negative number if the first object is less than the second, 
 *                   a positive number if the first object is greater than the second, 
 *                   or 0 if they are equal based on the specified key.
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
 * Executes a SQL query on a SQLite database, calling a callback function for each row returned by the query.
 * @param {Object} db - An SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - A callback function to be invoked for each row in the result set. The function will receive the current row as its parameter.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}