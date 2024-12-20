
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values at a specified key.
 * Returns -1 if the value of `a` at `keymap` is less than the value of `b` at `keymap`,
 * returns 1 if it is greater, and returns 0 if they are equal.
 *
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object for comparison.
 * @param {Object} b - The second object for comparison.
 * @returns {number} A comparison result: -1 if a < b, 1 if a > b, 0 if a === b.
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
 * Executes a given SQL query on the provided SQLite database and processes each result row with a callback function.
 * @param {Object} db - The SQLite database instance to run the query on.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The callback function to be called for each row of the query result. It receives the row data as its argument.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}