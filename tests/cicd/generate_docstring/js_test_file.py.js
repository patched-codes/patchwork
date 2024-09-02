
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQL query on a SQLite database and processes each result row with a callback.
 * @param {object} db - The SQLite database object.
 * @param {string} query - The SQL query to execute.
 * @param {function} callback - The callback function to process each result row.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of the specified key.
 * @param {string} keymap - The key to compare the values of the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value in `a` is less than the value in `b`, 
 *                     1 if the value in `a` is greater than the value in `b`, 
 *                     and 0 if the values are equal.
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