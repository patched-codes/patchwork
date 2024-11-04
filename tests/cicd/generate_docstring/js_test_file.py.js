
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and determines their sort order.
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a` is less than `b`, 1 if greater, and 0 if equal, based on the specified key.
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
 * Executes a provided SQL query on the specified SQLite database and invokes a callback function for each row in the result set.
 * @param {Object} db - An instance of the SQLite database.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The function to be called for each row in the result set, taking the row as an argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}