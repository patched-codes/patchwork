
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
 * Executes an SQL query on a SQLite database and applies a callback function to each result row.
 * @param {Object}  db - The SQLite database object.
 * @param {string}  query - The SQL query to be executed.
 * @param {Function} callback - The callback function to handle each row of query results.
 * @returns {void} This function doesn't return anything; it uses a callback to handle results.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and returns a comparison result.
 * @param {string} keymap - The key to be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of key in `a` is less than in `b`, 1 if greater, or 0 if equal.
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