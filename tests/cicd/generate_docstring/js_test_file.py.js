
/**
 * Adds two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query and processes each result row with a callback function.
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to execute.
 * @param {function} callback - The callback function to process each result row.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * 
 * @param {string} keymap - The key by which the objects `a` and `b` should be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a` at `keymap` is less than the value of `b` at `keymap`,
 *                    1 if greater, and 0 if they are equal.
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