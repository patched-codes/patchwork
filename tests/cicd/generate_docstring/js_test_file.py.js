
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and determines their sort order.
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if the value of the given key in the first object is less than that in the second.
 * Returns 1 if it is greater. Returns 0 if they are equal.
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
 * Executes a SQL query on a given SQLite database, applying a callback function on each resulting row.
 * @param {Object}  db - The SQLite database object on which the query will be executed.
 * @param {string}  query - The SQL query string to be executed.
 * @param {function} callback - A callback function that will be executed on each row resulting from the query. 
 * @returns {void} This function does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}