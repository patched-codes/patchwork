
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers provided.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and determines their order.
 * @param {string}  keymap - The key used to retrieve values from the objects for comparison.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a' is less than the value of 'b', 1 if greater, and 0 if they are equal.
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
 * Executes a SQL query against a database and processes each result row.
 * @param {Object} db - The database connection object to perform operations on.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {Function} callback - The function to call with each row returned by the query. The function receives two arguments: an error object and the current row of data.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}