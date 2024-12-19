
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
 * Compares two objects based on a specified key and returns a numeric value
 * indicating their relative order.
 * @param {string} keymap - The key on which the objects are compared.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} -1 if the first object is less than the second object, 1 if greater, and 0 if they are equal regarding the specified key.
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
 * Executes a SQL query on the given database and applies a callback function to each row of the result set.
 * @param {Object} db - The SQLite database object to execute the query on.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be called for each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}