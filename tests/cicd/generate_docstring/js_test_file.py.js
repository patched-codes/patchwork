
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key, returning a value to determine their relative ordering.
 * @param {string} keymap - The key in the objects `a` and `b` to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if `a[keymap]` is less than `b[keymap]`, 1 if `a[keymap]` is greater, and 0 if they are equal.
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
 * Executes a SQL query on a SQLite database and processes each row with a callback function.
 * @param {object}  db - The SQLite database object.
 * @param {string}  query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row in the result set.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}