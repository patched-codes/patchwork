
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key extracted from a keymap.
 * Returns -1 if the value of the specified key in object `a` is less than in object `b`,
 * Returns 1 if the value of the specified key in object `a` is greater than in object `b`,
 * Returns 0 if the values are equal.
 * 
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} A number indicating the sort order.
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
 * Executes an SQL query on a given database and applies a callback function to each row in the result set.
 * @param {Object}  db - The SQLite database object on which the query will be executed.
 * @param {string}  query - The SQL query to be executed on the database.
 * @param {function} callback - A function to be called for each row in the result set. It receives an error and a row object as arguments.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}