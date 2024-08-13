
/**
 * Takes two numbers as input and returns the sum of the two numbers.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite database query and invokes a callback function for each result row
 * @param {object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to be called for each result row
 * @returns {void} - No return value
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in a keymap.
 * @param {string} keymap - The key to use for comparison from the objects.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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