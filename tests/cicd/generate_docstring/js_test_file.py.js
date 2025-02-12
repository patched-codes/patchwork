
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value associated with a specific key.
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the value of the key in object 'a' is less than in object 'b', 1 if greater, and 0 if they are equal.
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
 * Executes a specified SQL query on a SQLite database and processes each result row using a callback function.
 * @param {Object} db - A SQLite database object that provides the `serialize` and `each` methods.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {Function} callback - A function to be called for each row in the result set, with the row data as the first argument and an error object as the second argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}