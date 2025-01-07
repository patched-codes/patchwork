
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key.
 * @param {string} keymap - The key name used to access the values in objects a and b for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if object a's value is less than object b's value, 1 if it's greater, and 0 if they are equal.
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
 * Executes a query on a SQLite database and processes each row with a callback function.
 * @param {Object}  db - The SQLite database object on which the query will be executed.
 * @param {string}  query - The SQL query to be executed on the database.
 * @param {function}  callback - The function to be called for each row resulting from the query.
 * @returns {void} Does not return any value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}