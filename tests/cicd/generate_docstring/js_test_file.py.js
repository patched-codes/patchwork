
/**
 * Computes the sum of two numbers.
 * @param {number}  a - The first number.
 * @param {number}  b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on a database and processes each row individually using a callback function.
 * 
 * @param {object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The function to be called for each row returned by the query.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a given key and returns an integer indicating their relative order.
 * @param {string} keymap - The key name used for comparing the two objects.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} - Returns -1 if the value of a[keymap] is less than b[keymap], 
 *                     1 if the value of a[keymap] is greater than b[keymap], 
 *                     and 0 if they are equal.
 */
const compare= function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}