
/**
 * Adds two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns an integer indicating their relative order.
 * @param {string} keymap - The key used to compare values in the objects 'a' and 'b'.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a[keymap]' is less than 'b[keymap]', 1 if greater, and 0 if equal.
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
 * Executes a SQL query on a provided SQLite database, processing each row with a callback function.
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row of the result set. It receives the row as a parameter.
 * @returns {void} No return value. The function operates asynchronously and utilizes a callback to process query results.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}