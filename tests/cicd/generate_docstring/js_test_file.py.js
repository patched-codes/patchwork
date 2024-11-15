
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
 * Compares two objects based on a specified key. 
 * Returns -1 if the value of the key in the first object is less than in the second, 
 * 1 if it is greater, and 0 if they are equal.
 * @param {string} keymap - The key name based on which the objects will be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1, 0, or 1 based on the comparison of the specified key values in the objects.
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
 * Executes a given SQL query on a specified SQLite database and applies a callback function on each result row.
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row of the result set, with the row data as the argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}