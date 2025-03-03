
/**
 * Adds two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specific key and returns a value indicating their order.
 * @param {string}  keymap - The key in both objects to use for comparison.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1 if the value of the key in object `a` is less than in object `b`, 
 *                    1 if greater, and 0 if they are equal.
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
 * Executes a SQL query on a given SQLite database and calls a callback function for each row in the result set.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {function} callback - The callback function to be called for each row retrieved by the query.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}