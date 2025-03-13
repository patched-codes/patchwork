
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
 * Compares two objects based on a specified property defined by the keymap.
 * Returns -1 if the property value of 'a' is less than that of 'b', 1 if greater, and 0 if equal.
 * 
 * @param {string} keymap - The key or property name to compare the values of.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], 0 if equal.
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
 * Executes a given query on the provided SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be called for each row of the query's result. 
 *                              It receives the current row as an argument.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}