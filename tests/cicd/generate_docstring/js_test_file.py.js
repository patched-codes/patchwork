
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key, and determines their order.
 * @param {string} keymap - The key on which to compare the objects.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the value of the first object is less than the second; 1 if greater; 0 if they are equal.
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
 * Executes a SQL query on a given SQLite database and applies a callback function to each row of the result.
 * @param {Object} db - The SQLite database instance to perform operations on.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - A function to be called for each row retrieved from the query execution.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}