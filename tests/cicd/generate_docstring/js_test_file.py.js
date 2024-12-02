
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
 * Compares two objects based on a specified key and determines their order.
 * @param {string} keymap - The key used to compare values between object 'a' and object 'b'.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if 'a' is less than 'b', 1 if 'a' is greater than 'b', or 0 if they are equal.
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
 * Executes a SQL query on the provided database and applies a callback function to each result row.
 * @param {Object} db - The database connection object on which the query will be executed.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be called for each row of the result set. Receives the current result row as an argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}