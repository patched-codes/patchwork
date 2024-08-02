
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two input numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the given SQLite query for each row in the database and calls the callback function.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQLite query to be executed
 * @param {Function} callback - The callback function to handle each row returned by the query
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key.
 * @param {string} keymap - The key to compare the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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