
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and returns a comparison result.
 * @param {string} keymap - The key used to compare the objects' properties.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the value of `a[keymap]` is less than `b[keymap]`, 
 *                     1 if the value of `a[keymap]` is greater than `b[keymap]`, 
 *                     and 0 if they are equal.
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
 * Executes an SQL query on a given database using the provided callback function
 * to handle each row of the result set.
 * @param {object} db - The SQLite database object to operate on.
 * @param {string} query - The SQL query string to execute.
 * @param {function} callback - The function to call for each row in the result set.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}