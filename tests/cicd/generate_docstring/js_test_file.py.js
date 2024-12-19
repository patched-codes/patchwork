
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key.
 * @param {string} keymap - The key used to access values in the objects for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a' is less than 'b', 1 if the value of 'a' is greater than 'b', and 0 if they are equal.
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
 * Executes a provided SQL query on the given SQLite database and calls the callback function for each row in the result set.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The callback function to be called for each row in the result set. It typically takes two arguments (error, row).
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}