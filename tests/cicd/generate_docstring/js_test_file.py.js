
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
 * Compares two objects based on the value at the specified key and determines their sort order.
 * @param {string} keymap - The key used to access the properties of the objects for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if `a` should appear before `b`, 1 if `a` should appear after `b`, and 0 if they are equal based on the specified key.
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
 * Executes a SQL query on a given SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be executed on each row returned by the query.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}