
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified property key.
 * @param {string} keymap - The property key used for comparison within the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of property `keymap` in object `a` is less than in object `b`,
 * 1 if it's greater, or 0 if they are equal.
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
 * Executes a query on the given SQLite database and processes each row of the result set with a callback function.
 * @param {Object} db - The SQLite database object to perform the query on.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The callback function to be called for each row of the query result. Receives the row object as an argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}