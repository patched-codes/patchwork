
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on a SQLite database and applies a callback function to each row in the result set.
 * @param {sqlite3.Database} db - The SQLite database instance.
 * @param {string} query - The SQL query to execute.
 * @param {function} callback - The function to apply to each row. It is called with the following parameters: (err: Error | null, row: object).
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if the value of `a[keymap]` is less than `b[keymap]`, 1 if greater, 0 if equal.
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