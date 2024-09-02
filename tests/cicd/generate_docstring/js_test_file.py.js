
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query using the provided SQLite database connection and processes each row of the result set with the specified callback function.
 * 
 * @param {Object} db - SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The function to be called for each row in the result set. The callback function takes the parameters (err, row), where 'err' is the possible error and 'row' is the current row.
 * @returns {void} This function does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * Returns -1 if the value of the specified key in the first object is less than that in the second object.
 * Returns 1 if the value of the specified key in the first object is greater than that in the second object.
 * Returns 0 if the values are equal.
 * 
 * @param {string} keymap - The key whose value is to be compared between the two objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1, 0, or 1 based on the comparison.
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