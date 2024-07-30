
/**
 * A function that returns the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on a SQLite database and calls a callback function for each row in the result set.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The query to be executed on the database
 * @param {Function} callback - The callback function to be called for each row in the result set
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the objects.
 * @param {string} keymap - The key to be used for comparison in the objects.
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