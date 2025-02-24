
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the specified key and returns a number indicating their order.
 * The function returns -1 if the value of the specified key in the first object is less than in the second, 
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} A number indicating the order of the objects based on the specified key. 
 *                   Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], or 0 if they are equal.
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
 * Executes a SQL query on the given database and applies the callback to each row of the result.
 * @param {Object} db - The SQLite database object to perform the query on.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - A function to be called for each row, with the row data as an argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}