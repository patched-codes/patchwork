
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on the provided SQLite database, invoking a callback for each row resulting from the query.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The function to be called for each row of the result set. It receives two arguments: err (the error, if any) and row (the current row).
 * @returns {void} Nothing is returned by this function.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key name to compare the values of.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], and 0 if they are equal.
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