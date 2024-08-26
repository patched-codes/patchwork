
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on a SQLite database and processes each row using a callback function.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to execute.
 * @param {function} callback - The callback function to process each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key.
 * @param {string} keymap - The key in the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a' is less than the value of 'b', 1 if the value of 'a' is greater than the value of 'b', and 0 if they are equal.
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