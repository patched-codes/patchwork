
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on a SQLite database and applies a callback function to each row in the result set.
 * @param {Object}  db - The SQLite database instance.
 * @param {string}  query - The SQL query to be executed.
 * @param {function}  callback - The callback function to be applied to each row in the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the keymap and returns a comparison result.
 * @param {string} keymap - The key used to compare the objects.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if `a` is less than `b`, 1 if `a` is greater than `b`, and 0 if they are equal.
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