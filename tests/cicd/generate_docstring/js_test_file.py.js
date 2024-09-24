
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
 * Executes a given SQL query on the provided SQLite database and processes each row of the result set.
 * 
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The callback function to be called for each row in the result set.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * 
 * @param {string} keymap - The key in the objects used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a[keymap]` is less than `b[keymap]`; 
 *                   1 if the value of `a[keymap]` is greater than `b[keymap]`; 
 *                   0 if the values are equal.
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