
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and determines their order.
 * @param {string} keymap - The key used to extract values from the objects for comparison.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} A negative number if the value from object 'a' is less than 'b', 
 *                   a positive number if the value from object 'a' is greater than 'b', 
 *                   or zero if they are equal.
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
 * Executes a SQL query on a database in serialized mode and applies a callback function for each result row.
 * @param {Object} db - The SQLite database object that connects to the database.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {function} callback - The function to be called for each row in the result set.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}